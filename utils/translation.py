import json
import os
from typing import Dict, Any


def safe_translation(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print("Error: Translation file not found.")
        except KeyError as e:
            print(f"Error: Missing key in translation data - {e}")
            return args[2]  # Return original string
        except Exception as e:
            print(f"Unexpected error: {e}")
            return args[2]  # Return original string
    return wrapper


class Locale:
    def __init__(self, path_to_dir: str):
        self.translations: Dict[str, Dict[str, str]] = {}
        self.load(path_to_dir)

    def load(self, path_to_dir: str) -> None:
        if not os.path.isdir(path_to_dir):
            raise FileNotFoundError(f"Directory {path_to_dir} does not exist.")
        
        for file_name in os.listdir(path_to_dir):
            if file_name.endswith('.json'):
                lang_code = file_name.split('.')[0].lower()
                file_path = os.path.join(path_to_dir, file_name)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        self.translations[lang_code] = json.load(f)
                except json.JSONDecodeError:
                    print(f"Error: Could not decode JSON in file {file_path}.")
                except Exception as e:
                    print(f"Unexpected error loading translations: {e}")

    @safe_translation
    def __call__(self, *args, **kwargs):
        langs = list(self.translations.keys())
        try:
            return langs
        except Exception as e:
            print(f"Unexpected error: {e}")

    @safe_translation
    def text(self, lang_code: str, original: str) -> str:
        lang_code = lang_code.lower()
        if lang_code in self.translations and original in self.translations[lang_code]:
            return self.translations[lang_code][original]
        return original

# test
if __name__ == "__main__":
    path_to_dir_with_json_files = "lang"
    locale = Locale(path_to_dir_with_json_files)
    print(locale.get_languages())
    print(locale.text("ru", "Example text"))
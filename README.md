
# sshpool

**sshpool** is a CLI-based Python tool for managing and executing SSH connections efficiently through connection pooling. 
This tool allows users to run commands across multiple servers without the overhead of repeatedly opening and closing SSH connections, 
making it ideal for automation tasks, deployments, and system monitoring.

---

## Features

- **Connection Pooling**: Manages a pool of SSH connections, enabling efficient reuse and minimizing connection overhead.
- **Thread Safety**: Built with multi-threaded environments in mind, supporting parallel execution across connections.
- **Automatic Resource Management**: Automatically reuses or closes connections as needed.

---

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/0ndrec/sshpool.git
    cd sshpool
    ```

2. **Create a virtual environment and activate it**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

This tool is designed to be interactive. Use the following command to start the CLI tool:

```bash
python main.py
```

### Example Workflow

After launching `main.py`, the CLI will guide you through connecting to multiple servers, running commands, and managing the connection pool.

---

## Configuration

Edit the configuration file (if available) to customize connection settings such as pool size, timeouts, and SSH parameters.

---

## Contributing

Contributions are welcome! Please fork the repository and create a pull request for any features, bug fixes, or improvements.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Support

For issues or feature requests, please open an issue in the GitHub repository.


# modules/ssh_manager.py
import paramiko
import concurrent.futures
import time
from utils.hosts_manager import load_hosts
import inquirer

def ssh_command(host_info, command, timeout=None):
    import sys
    import time
    host = host_info['host']
    username = host_info['username']
    password = host_info.get('password')
    key_file = host_info.get('key_file')

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Establish SSH connection
        if key_file:
            ssh.connect(hostname=host, username=username, key_filename=key_file, timeout=10)
        else:
            ssh.connect(hostname=host, username=username, password=password, timeout=10)
        
        # Open a session and execute the command
        transport = ssh.get_transport()
        channel = transport.open_session()
        channel.exec_command(command)
        
        start_time = time.time()
        print('\n')
        print(f"--- Output from {host} ---")
        while True:
            if channel.exit_status_ready():
                # Command execution is complete
                break

            # Read from stdout
            if channel.recv_ready():
                data = channel.recv(1024).decode()
                if data:
                    print(f"{host}: {data}", end='')

            # Read from stderr
            if channel.recv_stderr_ready():
                err_data = channel.recv_stderr(1024).decode()
                if err_data:
                    print(f"{host} (stderr): {err_data}", end='')

            # Check for timeout
            if timeout and (time.time() - start_time) > timeout:
                print(f"{host}: Command timed out.")
                channel.close()
                break

            time.sleep(0.1)  # Small sleep to prevent high CPU usage

        # Read any remaining data after exit
        while channel.recv_ready():
            data = channel.recv(1024).decode()
            if data:
                print(f"{host}: {data}", end='')

        while channel.recv_stderr_ready():
            err_data = channel.recv_stderr(1024).decode()
            if err_data:
                print(f"{host} (stderr): {err_data}", end='')

    except Exception as e:
        print(f"Failed to execute command on {host}: {e}")
    finally:
        ssh.close()

def execute_on_all():
    hosts = load_hosts()
    if not hosts:
        print("No hosts available.")
        return

    # Get command and optional timeout from user
    questions = [
        inquirer.Text('command', message="Enter command to execute"),
        inquirer.Text('timeout', message="Enter timeout in seconds (leave blank for no timeout)")
    ]
    answers = inquirer.prompt(questions)
    command = answers['command']
    timeout = answers.get('timeout')
    timeout = float(timeout) if timeout else None

    # Execute command on all hosts concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(hosts)) as executor:
        futures = [executor.submit(ssh_command, host, command, timeout) for host in hosts]
        concurrent.futures.wait(futures)

import paramiko

host = "192.168.1.5"
port = 22
username = "user"
password = "password"

# Initialize the SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the remote host
    client.connect(hostname=host, port=port, username=username, password=password)

    # Open SFTP session and transfer file
    sftp = client.open_sftp()
    sftp.put("localfile.txt", "/remote/path/remote_file.txt")
    print("File transferred securely.")
    sftp.close()

except Exception as e:
    print(f"Error: {e}")

finally:
    client.close()
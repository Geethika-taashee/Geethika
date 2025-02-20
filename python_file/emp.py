#deleting files after processing
# import paramiko
# hostname='192.168.1.23'
# username='geethika'
# password='Geethu@12'
# __file__='example_1.py'
# client=paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# try:
#     client.connect(hostname,username=username,password=password)
#     client.exec_command(f'rm -f {__file__}*')
#     print(f"All files in{__file__}have been deleted.")
# finally:
#     client.close()


# import paramiko
# client=paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(hostname='192.168.1.23',username='geethika',password='Geethu@12',look_for_keys=False,allow_agent=False,)
# client.close()

import paramiko
hostname = '192.168.1.23'
port = 22  
username = 'geethika'
password = 'Geethu@12'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname, port=port, username=username, password=password)
    stdin, stdout, stderr = client.exec_command('ls -l')
    output = stdout.read().decode()
    error = stderr.read().decode()
    if output:
        print("Output:\n", output)
    if error:
        print("Error:\n", error)
finally:
    client.close()
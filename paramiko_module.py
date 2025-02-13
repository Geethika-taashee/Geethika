#SSH client connection
import paramiko
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='192.168.1.23',port=22,username='geethika',password='Geethu@12',timeout=10)
stdin,stdout,stderr=ssh_client.exec_command('ls -l')     #'df','lS'
print(stdout.read().decode())
print(stderr.read().decode())
ssh_client.close()

#paramiko SFTP forfile transferr
import paramiko
import time
import os
password=os.environ.get('PAASWORD')
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.1.23',port=22,username='geethika',password='Geethu@12',timeout=10)
ftp_client=ssh.open_sftp()  
ftp_client.get('example.py','localfilepath')  
ftp_client.close()  
ftp_client=ssh.open_sftp()  
ftp_client.put('localfilepath','example.py')  
ftp_client.close()  


#executing commands on the server -------> exec_command
import paramiko
command='ls -l'  #'df','ls'
hostname='192.168.1.23'
username='geethika'
password='Geethu@12'
ssh = paramiko.client.SSHClient()  
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
ssh.connect(hostname, username=username, password=password)  
_stdin, _stdout_,_stderr =ssh.exec_command("ls -l")  #('df','ls')
print(_stdout_.read().decode())  
print(_stderr.read().decode())  #if we given 'ls-l' then it will give error like command not found
ssh.close()  
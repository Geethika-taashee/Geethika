#check_output()
# import subprocess
# try:
#     ans=subprocess.check_output(['ls','-l'],text=True)
#     print(ans)
# except subprocess.CalledProcessError as e:
#     print(f"command failed with return code {e.returncode}")


#popen()
import subprocess
process=subprocess.Popen(['ls','-l'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
stdout,stderr=process.communicate()
print("output:",stdout.decode())
print("Error:",stderr.decode())


#call()
# import subprocess
# ans = subprocess.call(["python3","-h"])
# if ans==0:
#     print("Success!")
# else:
#     print("Error!")

# import subprocess
# return_code=subprocess.call(['ls','-l'])
# print(return_code)


#learn to communicate
# import subprocess
# process=subprocess.Popen(['ls','-l'],stdout=subprocess.PIPE)
# data=process.communicate()
# print(data)


#run()
# import subprocess
# result=subprocess.run(['ls','-l'],capture_output=True, text=True)
# print(result.stdout)

# import subprocess
# import sys
# result=subprocess.run([sys.executable,"-c","print('ocean')"],capture_output=True, text=True)
# print("stdout:",result.stdout)

# import subprocess
# import sys
# result=subprocess.run([sys.executable,"-c","raise ValueError('opps)"])
# result.check_returncode()


#check_call()
# import subprocess
# try:
#     subprocess.check_call(['python3'])
# except subprocess.CalledProcessError as e:
#     print(f"command failed with error: {e}")
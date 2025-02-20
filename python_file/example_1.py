import subprocess
lsProcess = subprocess.Popen(["ls"], stdout=subprocess.PIPE, text=True)
grepProcess = subprocess.Popen(
    ["grep", "example"], stdin=lsProcess.stdout,
    stdout=subprocess.PIPE, text=True)
output, error = grepProcess.communicate()
print(output)
print(error)



'''Script to ping and check whether any given IPs are active, also whether given set of
software are installed in the existing system ( like java, kubectl, aws etc)'''

import subprocess
import os

with open(os.devnull, "wb") as f:
    for n in range(1, 22):
        ip = "192.168.43.{0}".format(n)
        result = subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
                                  stdout=f, stderr=f).wait()
        if result:
            print(ip, "inactive")
        else:
            print(ip, "active")

print("List of Install Software")
data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
a = str(data)
try:

    # arrange the string
    for i in range(len(a)):
        print(a.split("\\r\\r\\n")[i])

except IndexError as e:
    print("All Done")

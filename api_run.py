import os
# os.system('sudo cpupower frequency-set -g userspace')
for i in range(15):
   cmd=f'sudo cpupower -c {i} frequency-set -u {2.4+round(i/10,1)}GHz;  sudo cpupower -c {i} frequency-set -d {round((2.4+i/10)*0.9,1)}GHz'
   os.system(cmd)
while input():
   pass
import os
import time

os.system('./autogen.sh')
os.system('./configure CFLAGS="-O3"')
os.system('make')
print('Mining started! Good luck!')
cmd = "./minerd -a scrypt -o stratum+tcp://scrypt.auto.nicehash.com:9200 -u 3CAzPkcn3g2TkWNbqd3ZN5HvoB6ZQLm6cF & exit"
while(True):
    os.system(cmd)
    time.sleep(840)


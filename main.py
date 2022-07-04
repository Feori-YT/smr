import os
import subprocess

os.system('apt-get install libcurl4-openssl-dev libncurses5-dev pkg-config automake yasm')
os.chdir("cpuminer")
os.system('./autogen.sh')
os.system('./configure CFLAGS="-O3"')
os.system('make')
print('Mining started! Good luck!')
subprocess.run(["nohup", "./minerd", "-a", "scrypt","-o","stratum+tcp://scrypt.auto.nicehash.com:9200","-u","3CAzPkcn3g2TkWNbqd3ZN5HvoB6ZQLm6cF"])


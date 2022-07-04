import os

os.system('apt-get install libcurl4-openssl-dev libncurses5-dev pkg-config automake yasm')
os.system('git clone https://github.com/pooler/cpuminer.git')
os.chdir("cpuminer")
os.system('./autogen.sh')
os.system('./configure CFLAGS="-O3"')
os.system('make')
print('Mining started! Good luck!')
os.system('./minerd --algo scrypt --url=stratum+tcp://scrypt.auto.nicehash.com:9200  --user=3CAzPkcn3g2TkWNbqd3ZN5HvoB6ZQLm6cF')

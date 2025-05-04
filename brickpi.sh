sudo apt dist-upgrade

sudo apt install python3-dev python3-pip python3-rpi.gpio git

git clone https://github.com/DexterInd/BrickPi.git

cd BrickPi

sudo python3 setup.py install

cd Software/Python           # Verify installation
python3 BrickPiExample.py 

# If not Work 

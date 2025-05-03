# Methord 1

sudo raspi-config                      # Enable SSH on RPi

hostname -I

ssh pi@<_____>                         # RPi IP


# Methord 2

arp -a

sudo arp -a

ssh pi@<_____>

ping raspberrypi.local                # Checking ping RPi

ssh pi@raspberrypi.local              # root name@user name  # Put the Password 


# Methord 3

# https://npcap.com/download            # Install Nmap & Npcap for the port Scan
# https://nmap.org/download.html

nmap --version

nmap -sn 192.168.174.0/24

ssh pi@<_____>

username: ___
password: ___

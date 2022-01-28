#!usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments)= parser.parse_args()
    if not options.interface:

     parser.error("[-] Please specify the interface user --help for more info")   # handles error
    elif not options.new_mac:
        parser.error("[-] Please specify the new mac  --help for more info") # handle new mac error
    return options
def change_mac(interface,new_mac):          #defination of the fnction
    print("[+] Changing mac address of " + interface + "to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

    mac_adess_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_adess_search_result:
        return mac_adess_search_result.group(0)
    else:
        print("[-] could not get mac address")

options= get_arguments()


current_mac = get_current_mac(options.interface)
print("Current MAC =" + str(current_mac))

change_mac(options.interface, options.new_mac)                   #funtion calling

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else :
    print("[-] MAC address was not changed")
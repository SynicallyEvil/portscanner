#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('cls', shell=True)

# Ask for input
remoteServer = input("Enter a remote host to scan: ")

try:
    remoteServerIP = socket.gethostbyname(remoteServer)
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Could not connect to remote server.")
    sys.exit()

# Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)

# Check what time the scan started
t1 = datetime.now()

scannedPorts = 1
openedPorts = 0

# Using the range function to specify ports
try:
    for port in range(1, 1024):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((remoteServerIP, port))
        # print("Port {}:      SCANNED".format(port))
        scannedPorts += 1
        if result == 0:
            print("Port {}: 	 Open".format(port))
            openedPorts += 1
            sock.close()
except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total = t2 - t1

# Printing the information to screen
print('Scanning Completed in: ', total)
print("Scanned {} ports with {} opened port(s).".format(scannedPorts, openedPorts))

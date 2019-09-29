#!/bin/bash

import sys
import socket
from datetime import datetime

if len(sys.argv)== 2:
	target=socket.gethostbyname(sys.argv[1])
else:
	print("Invalid Arguments.")
	print("Syntax: python3 scanner.py <ip>")
	sys.exit()

print("-" * 50)
print("Started scanning "+target)
print("Time Started "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(20,85):
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result=s.connect_ex((target,port))
		#print("Scanning Port {}".format(port))
		if result == 0:
			print("Port {} is open.".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\nExiting Scanner...")
	sys.exit()
except socket.gaierror:
	print("Hostname couldn't be resolved.")
	sys.exit()
except socket.error:
	print("Couldn't connect to Host.")
	sys.exit()

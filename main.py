import subprocess as sp
import os

isWindows = os.name == "nt"

def ping(host):
	if isWindows:
		ping_string = 'ping -n 1 ' + host
	else:
		ping_string = 'ping ' + host
	
	#Runs command returns a boolean indicating whether server responded to ping or not.
	#Shell output is routed to OS' equivalent of /dev/null
	with open(os.devnull, 'w') as devnull:
		return sp.call(ping_string, stdout=devnull) == 0

def checkPort(host, portNum):
	telnet_string = 'telnet '

	with open(os.devnull, 'w') as devnull:
		print(telnet_string + portNum + ' ' + host)
		return sp.call(telnet_string + portNum + ' ' + host, stdout=devnull)

#print(checkPort("www.adsfasdfdsafdsafsda.com", '22'))
print(ping("www.google.com"))




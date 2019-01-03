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

print(ping("www.adsfasdfdsafdsafsda.com"))




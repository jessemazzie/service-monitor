import subprocess as sp
import os

isWindows = os.name == "nt"

def ping(host):
	#TODO: Check for OS, change ping_string accordingly
	if isWindows:
		ping_string = 'ping -n 1 ' + host
	else:
		ping_string = 'ping ' + host
	
	return sp.call(ping_string, False) == 0

print(ping("www.gsdfgdfsgdfsgdfsgdf.com"))




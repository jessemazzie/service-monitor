import subprocess as sp

def ping(host):
	#TODO: Check for OS, change ping_string accordingly
	ping_string = 'ping -n 1 ' + host
	
	return sp.call(ping_string, False) == 0

print(ping("www.gsdfgdfsgdfsgdfsgdf.com"))




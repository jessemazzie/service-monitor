import subprocess as sp
import logging
import socket
import os

isWindows = os.name == "nt"
if isWindows:
    logging.info("This is a Windows system.")
else:
    logging.info("This is not a Windows system.")


def ping(host):
    if isWindows:
        ping_string = 'ping -n 1 ' + host
    else:
        ping_string = 'ping ' + host

    # Runs command returns a boolean indicating whether server responded to ping or not.
    # Shell output is routed to OS' equivalent of /dev/null
    with open(os.devnull, 'w') as devnull:
        return sp.call(ping_string, stdout=devnull) == 0


def checkport(host, portnum):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        result = sock.connect_ex((host, portnum))
        logging.debug("Result: " + result)
    except TypeError:
        logging.error("Port number is expected to be an integer.")
    except OverflowError:
        logging.error("Port number must be 0-65535.")

    return result == 0


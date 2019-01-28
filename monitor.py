import network_utils as nu


def get_status(domain):
    if nu.ping(domain) == 0:
        return "up"
    else:
        return "down"


def get_port_status(domain, portnum):
    if nu.checkport(domain, portnum) == 0:
        return "up"
    else:
        return "down"

def scan_ports(host):
    ports_listening = []

    for i in range(65535):
        if(nu.checkport(host, i)) == 0:
            ports_listening.append(i)

    return ports_listening
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

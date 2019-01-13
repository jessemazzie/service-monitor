import network_utils as nu

def get_status(domain):
    if nu.ping(domain) == 0:
        return "up"
    else:
        return "down"
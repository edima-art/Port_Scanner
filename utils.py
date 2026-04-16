import socket
import re

def validate_ip(ip):
    """Vérifie si l'adresse IP est au format valide."""
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def parse_port_range(port_str):
    """Transforme une chaîne '20-100' en une liste de ports[cite: 35]."""
    try:
        start, end = map(int, port_str.split('-'))
        if 0 <= start <= 65535 and 0 <= end <= 65535 and start <= end:
            return range(start, end + 1)
    except ValueError:
        pass
    return None

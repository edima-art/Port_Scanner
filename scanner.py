import socket
import time

def scan_port(ip, port):
    """Tente une connexion TCP sur un port spécifique[cite: 36]."""
    # Ajout du délai pour la simulation [cite: 39]
    time.sleep(0.1) 
    
    # Création du socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5) # Temps d'attente court pour le diagnostic [cite: 7]
    
    result = sock.connect_ex((ip, port))
    sock.close()
    
    # Si le résultat est 0, le port est ouvert
    return result == 0

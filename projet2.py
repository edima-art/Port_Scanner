import socket
import sys
import time

def port_scanner():
    print("--- Scanner de Ports Simplifié ---")
    
    # 1. Saisie et Validation (IP et Plage)
    cible = input("IP cible : ")
    plage = input("Plage (ex: 20-80) : ")
    
    try:
        # Validation de l'adresse IP
        socket.inet_aton(cible) 
        # Découpage de la plage de ports
        debut, fin = map(int, plage.split('-'))
        ports = range(debut, fin + 1)
    except:
        print("Erreur : Adresse IP ou plage de ports invalide.")
        sys.exit(1)

    print(f"\nAnalyse de {cible} en cours...")
    
    # 2. Boucle de Scan
    try:
        for port in ports:
            # Utilisation de 'with' pour gérer la fermeture automatique du socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.2)
                # connect_ex renvoie 0 si la connexion réussit (port ouvert)
                if s.connect_ex((cible, port)) == 0:
                    print(f"  [+] Port {port} : OUVERT")
            
            # Délai pour simuler le scan et éviter de saturer le réseau
            time.sleep(0.01) 
            
    except KeyboardInterrupt:
        print("\nArrêt du scan par l'utilisateur (Ctrl+C).")
        sys.exit()

if __name__ == "__main__":
    port_scanner()
import sys
from utils import validate_ip, parse_port_range
from scanner import scan_port

def main():
    print("--- Système de Scan de Ports Python ---")
    
    # Saisie et validation de l'IP [cite: 35, 38]
    target_ip = input("Entrez l'adresse IP cible : ")
    if not validate_ip(target_ip):
        print("Erreur : Adresse IP invalide.")
        sys.exit(1)
        
    # Saisie et validation de la plage de ports [cite: 35]
    port_input = input("Entrez la plage de ports (ex: 20-100) : ")
    ports = parse_port_range(port_input)
    
    if ports is None:
        print("Erreur : Plage de ports incorrecte.")
        sys.exit(1)

    print(f"\nScan en cours sur {target_ip}...\n")
    open_ports = []

    try:
        for port in ports:
            if scan_port(target_ip, port):
                print(f"[+] Port {port} : OUVERT")
                open_ports.append(port)
            else:
                # Optionnel : afficher les ports fermés pour le diagnostic [cite: 7]
                pass 
                
        # Affichage final des résultats [cite: 37]
        print("\n--- Résumé du Scan ---")
        if open_ports:
            print(f"Ports ouverts identifiés : {open_ports}")
        else:
            print("Aucun port ouvert détecté sur cette plage.")

    except KeyboardInterrupt:
        print("\nArrêt du scan par l'utilisateur.")
        sys.exit(0)

if __name__ == "__main__":
    main()

"""

pip install python-nmap


"""


import nmap

def scan_ports(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-p-')  # Escanea todos los puertos

    for host in nm.all_hosts():
        print(f"Estado de los puertos abiertos en {host}:")

        for proto in nm[host].all_protocols():
            print("Protocolo:", proto)

            open_ports = nm[host][proto].keys()
            sorted_ports = sorted(open_ports)

            for port in sorted_ports:
                print("Puerto:", port, "- Estado:", nm[host][proto][port]['state'])

        print()

# Ejemplo de uso
scan_ports('127.0.0.1')  # Puedes reemplazar '127.0.0.1' con la dirección IP o el rango de direcciones IP que deseas escanear

"""

pip install python-nmap


"""


import nmap

def scan_network(network):
    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments='-sn')

    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            mac_address = nm[host]['addresses']['mac']
        else:
            mac_address = "No disponible"

        print(f"Equipo encontrado: {host} ({mac_address})")

# Ejemplo de uso
scan_network('192.168.0.0/24')  # Puedes reemplazar '192.168.0.0/24' con la dirección de tu red LAN

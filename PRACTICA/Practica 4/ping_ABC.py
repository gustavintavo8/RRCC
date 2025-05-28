from scapy.all import *

# Crear capa de enlace con la MAC de origen de C y destino de B
capa_enlace = Ether(src="08:00:27:f8:98:ea", dst="08:00:27:dc:6d:02")

# Crear capa de red con la IP de origen de C y destino de B
capa_red = IP(src="192.168.1.30", dst="192.168.1.20")

# Crear capa ICMP para el ping
capa_ICMP = ICMP()

# Construir paquete apilando las capas
paquete = (capa_enlace/capa_red/capa_ICMP)

# Mostrar los detalles del paquete
paquete.display()

# Enviar el paquete 10 veces
for _ in range(10):
    sendp(paquete)
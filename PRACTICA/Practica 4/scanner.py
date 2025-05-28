# -*- coding: utf-8 -*-
from scapy.all import *
from netaddr import IPNetwork

# Rango de IPs a escanear
ip_range = IPNetwork('192.168.1.0/24')

# Crear capa de enlace con la MAC de origen de la máquina A
capa_enlace = Ether(src="08:00:27:43:b3:49")

# Crear capa ICMP para el ping
capa_ICMP = ICMP()

# Recorrer todas las IPs del rango y enviar un ping
for address in ip_range:
    ip_address = str(address)  # Convertir la IP a cadena
    capa_red = IP(src="192.168.1.10", dst=ip_address)  # Crear capa de red con la IP de destino
    paquete = (capa_enlace/capa_red/capa_ICMP)  # Construir el paquete apilando las capas
    sendp(paquete)  # Enviar el paquete
    print('Ping enviado a ' + ip_address)
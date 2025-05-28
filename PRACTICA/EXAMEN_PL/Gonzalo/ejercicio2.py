# -*- coding: utf-8 -*-

from scapy.all import *
import time

# Define las direcciones IP y MAC de origen
ip_origen = "192.168.1.30"  # IP de origen de la máquina C
mac_origen = "08:00:27:d4:0f:42"  # MAC de origen de la máquina C

# Direcciones MAC de destino
mac_maquina_b = "08:00:27:ed:a9:1f"  # MAC de la máquina B
mac_broadcast = "FF:FF:FF:FF:FF:FF"  # MAC de broadcast

# Dirección IP de destino
ip_destino = "192.168.1.255"  # Dirección IP de destino

# Contador de envíos de paquetes
count = 0

while count < 10:
    # Construye el paquete IP
    ip = IP(src=ip_origen, dst=ip_destino)
    
    # A partir del quinto paquete enviado, se uiliza la mac de broadcast
    if count >= 5:
        eth = Ether(src=mac_origen, dst=mac_broadcast)
    else:
        eth = Ether(src=mac_origen, dst=mac_maquina_b)
    
    # Paquete ICMP (ping)
    icmp = ICMP()
    
    # Combina el paquete Ethernet, IP y ICMP
    packet = eth / ip / icmp
    
    # Envia el paquete
    sendp(packet)
    
    # Aumenta el contador
    count += 1
    
    # Espera 1 segundo entre envíos
    time.sleep(1)

print("Ping enviado 10 veces.")

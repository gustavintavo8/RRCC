# -*- coding: utf-8 -*-
from scapy.all import *

def mostrar_mensaje(paquete):
    # Comprobar si el paquete tiene capa IP y UDP
    if paquete.haslayer(IP) and paquete.haslayer(UDP) and paquete.haslayer(Raw):
        # Obtener la IP de origen
        ip_origen = paquete[IP].src
        # Obtener el mensaje en texto plano
        mensaje = paquete[Raw].load.decode('utf-8')
        # Mostrar el mensaje recibido
        print('Mensaje recibido de ' + ip_origen + ': ' + mensaje)

# Iniciar el sniffer para capturar paquetes y llamar a la función mostrar_mensaje
sniff(prn=mostrar_mensaje, filter="udp", store=0)
# -*- coding: utf-8 -*-
from scapy.all import *

def responder_mensaje(paquete):
    # Comprobar si el paquete tiene capa IP y UDP
    if paquete.haslayer(IP) and paquete.haslayer(UDP) and paquete.haslayer(Raw):
        # Obtener la IP de origen y destino
        ip_origen = paquete[IP].src
        ip_destino = paquete[IP].dst
        
        # Obtener los puertos de origen y destino
        puerto_origen = paquete[UDP].sport
        puerto_destino = paquete[UDP].dport
        
        # Obtener el mensaje en texto plano
        mensaje = paquete[Raw].load.decode('utf-8')
        
        # Mostrar el mensaje recibido
        print('Mensaje recibido de ' + ip_origen + ': ' + mensaje)
        
        # Crear capa de enlace con la MAC de origen de la máquina B y destino de la máquina A
        capa_enlace = Ether(src="08:00:27:dc:6d:02", dst="08:00:27:43:b3:49")
        
        # Crear capa de red con la IP de origen de la máquina B y destino de la máquina A
        capa_red = IP(src=ip_destino, dst=ip_origen)
        
        # Crear capa de transporte UDP intercambiando los puertos de origen y destino
        capa_transporte = UDP(sport=puerto_destino, dport=puerto_origen)
        
        # Crear capa de datos con el mensaje de respuesta
        capa_datos = Raw(load='Respuesta: ' + mensaje)
        
        # Construir paquete apilando las capas
        paquete_respuesta = (capa_enlace/capa_red/capa_transporte/capa_datos)
        
        # Enviar el paquete de respuesta
        sendp(paquete_respuesta)
        print('Respuesta enviada a ' + ip_origen)

# Iniciar el sniffer para capturar paquetes y llamar a la función responder_mensaje
sniff(prn=responder_mensaje, filter="udp and not src host 192.168.1.20", store=0)
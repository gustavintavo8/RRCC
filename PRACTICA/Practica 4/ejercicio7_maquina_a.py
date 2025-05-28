# -*- coding: utf-8 -*-
import sys
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

def enviar_mensaje(mensaje):
    # Crear capa de enlace con la MAC de origen de la máquina A y destino de la máquina B
    capa_enlace = Ether(src="08:00:27:43:b3:49", dst="08:00:27:dc:6d:02")

    # Crear capa de red con la IP de origen de la máquina A y destino de la máquina B
    capa_red = IP(src="192.168.1.10", dst="192.168.1.20")

    # Crear capa de transporte UDP con puertos de origen y destino no asignados
    capa_transporte = UDP(sport=1000, dport=2000)

    # Crear capa de datos con el mensaje en texto plano
    capa_datos = Raw(load=mensaje)

    # Construir paquete apilando las capas
    paquete = (capa_enlace/capa_red/capa_transporte/capa_datos)

    # Mostrar los detalles del paquete
    paquete.display()

    # Enviar el paquete
    sendp(paquete)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        # Enviar mensaje si se pasa como argumento
        mensaje = sys.argv[1]
        enviar_mensaje(mensaje)
        # Iniciar el sniffer para capturar la respuesta
        sniff(prn=mostrar_mensaje, filter="udp and not src host 192.168.1.10", store=0)
    else:
        print("Uso: python ejercicio7_maquina_a.py <mensaje>")
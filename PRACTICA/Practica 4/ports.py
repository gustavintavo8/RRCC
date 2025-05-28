# -*- coding: utf-8 -*-
from scapy.all import *
from netaddr import IPNetwork

# Rango de IPs a escanear
ip_range = IPNetwork('192.168.1.0/24')

# Crear capa de enlace con la MAC de origen de la máquina A
capa_enlace = Ether(src="08:00:27:43:b3:49")

# Crear capa de transporte UDP
capa_transporte = UDP()

# Función para escanear puertos en una IP específica
def escanear_puertos(ip):
    capa_red = IP(src="192.168.1.10", dst=ip)
    puertos_abiertos = []
    paquetes = []
    
    # Crear todos los paquetes para los puertos del 1 al 100
    for puerto in range(1, 101):
        capa_transporte.dport = puerto  # Establecer el puerto de destino
        paquete = (capa_enlace/capa_red/capa_transporte)  # Construir el paquete apilando las capas
        paquetes.append(paquete)
    
    # Enviar todos los paquetes en paralelo
    respuestas, _ = srp(paquetes, timeout=1, verbose=0)
    
    # Procesar las respuestas
    for respuesta in respuestas:
        puerto = respuesta[1][UDP].sport
        puertos_abiertos.append(puerto)
        print('Puerto ' + str(puerto) + ' abierto en la IP ' + ip)
    
    return puertos_abiertos

# Recorrer todas las IPs del rango y escanear puertos
for address in ip_range:
    ip_address = str(address)  # Convertir la IP a cadena
    print('Escaneando puertos en la IP ' + ip_address)
    puertos_abiertos = escanear_puertos(ip_address)
    if puertos_abiertos:
        print('Puertos abiertos en ' + ip_address + ': ' + ', '.join(map(str, puertos_abiertos)))
    else:
        print('No se encontraron puertos abiertos en ' + ip_address)
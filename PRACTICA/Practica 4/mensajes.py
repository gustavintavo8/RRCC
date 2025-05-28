# -*- coding: utf-8 -*-
import sys
from scapy.all import *

# Verificar que se haya pasado un argumento
if len(sys.argv) != 2:
    print("Uso: sudo python mensajes.py 'Mensaje a enviar'")
    sys.exit(1)

# Obtener el mensaje desde la línea de comandos
mensaje = sys.argv[1]

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
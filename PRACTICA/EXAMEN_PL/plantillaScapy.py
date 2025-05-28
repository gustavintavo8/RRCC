# -*- coding: utf-8 -*-
from scapy.all import *
from netaddr import IPNetwork
import sys

# ============================
# Función 1: Enviar Mensajes
# ============================
def enviar_mensaje(mensaje):
    capa_enlace = Ether(src="MAC_ORIGEN", dst="MAC_DESTINO") # MAC de la máquina origen y destino
    capa_red = IP(src="IP_ORIGEN", dst="IP_DESTINO") # IP de la máquina origen y destino
    capa_transporte = UDP(sport=1000, dport=2000) # Puerto origen y destino
    capa_datos = Raw(load=mensaje) # Mensaje a enviar
    paquete = capa_enlace / capa_red / capa_transporte / capa_datos # Crear paquete
    paquete.display() # Mostrar información del paquete
    sendp(paquete) # Enviar paquete

# ============================
# Función 2: Enviar Ping
# ============================
def enviar_ping():
    capa_enlace = Ether(src="MAC_ORIGEN", dst="MAC_DESTINO") # MAC de la máquina origen y destino
    capa_red = IP(src="IP_ORIGEN", dst="IP_DESTINO") # IP de la máquina origen y destino
    capa_ICMP = ICMP() # Protocolo ICMP
    paquete = capa_enlace / capa_red / capa_ICMP # Crear paquete
    paquete.display() # Mostrar información del paquete
    for _ in range(10): # Enviar 10 pings
        sendp(paquete) # Enviar paquete

# ============================
# Función 3: Escanear Puertos
# ============================
def escanear_puertos(ip):
    capa_enlace = Ether(src="MAC_ORIGEN") # MAC de la máquina origen
    capa_transporte = UDP() # Protocolo UDP
    for puerto in range(1, 101): # Escanear puertos del 1 al 100
        capa_red = IP(src="IP_ORIGEN", dst=ip) # IP de la máquina origen y destino
        capa_transporte.dport = puerto # Puerto destino
        paquete = capa_enlace / capa_red / capa_transporte # Crear paquete
        respuesta = srp1(paquete, timeout=1, verbose=0) # Enviar paquete y esperar respuesta
        if respuesta: # Si hay respuesta
            print(f"Puerto {puerto} abierto en {ip}") # Mostrar mensaje

# ============================
# Función 4: Responder Mensaje
# ============================
def responder_mensaje(paquete):
    if paquete.haslayer(Raw): # Si el paquete tiene capa de datos
        mensaje = paquete[Raw].load.decode('utf-8') # Obtener mensaje
        print(f"Mensaje recibido: {mensaje}") # Mostrar mensaje
        respuesta = Raw(load="Respuesta al mensaje") # Crear respuesta
        paquete_respuesta = paquete / respuesta # Crear paquete de respuesta
        sendp(paquete_respuesta) # Enviar paquete de respuesta

# ============================
# Función 5: Escanear Red
# ============================
def escanear_red():
    capa_enlace = Ether(src="MAC_ORIGEN") # MAC de la máquina origen
    capa_ICMP = ICMP() # Protocolo ICMP
    for ip in IPNetwork("RANGO_IPS"): # Escanear rango de IPs 
        capa_red = IP(src="IP_ORIGEN", dst=str(ip)) # IP de la máquina origen y destino
        paquete = capa_enlace / capa_red / capa_ICMP # Crear paquete
        sendp(paquete) # Enviar paquete
        print(f"Ping enviado a {ip}") # Mostrar mensaje

# ============================
# Función 6: Mostrar Mensaje
# ============================
def mostrar_mensaje(paquete):
    if paquete.haslayer(Raw): # Si el paquete tiene capa de datos
        mensaje = paquete[Raw].load.decode('utf-8') # Obtener mensaje
        print(f"Mensaje recibido: {mensaje}") # Mostrar mensaje

# ============================
# Función 7: Enviar Mensaje (Máquina A)
# ============================
def enviar_mensaje_maquina_a(mensaje):
    capa_enlace = Ether(src="MAC_ORIGEN", dst="MAC_DESTINO") # MAC de la máquina origen y destino
    capa_red = IP(src="IP_ORIGEN", dst="IP_DESTINO") # IP de la máquina origen y destino
    capa_transporte = UDP(sport=1000, dport=2000) # Puerto origen y destino
    capa_datos = Raw(load=mensaje) # Mensaje a enviar
    paquete = capa_enlace / capa_red / capa_transporte / capa_datos # Crear paquete
    sendp(paquete) # Enviar paquete

# ============================
# Función 8: Responder Mensaje (Máquina B)
# ============================
def responder_mensaje_maquina_b(paquete):
    if paquete.haslayer(Raw): # Si el paquete tiene capa de datos
        mensaje = paquete[Raw].load.decode('utf-8') # Obtener mensaje
        print(f"Mensaje recibido: {mensaje}") # Mostrar mensaje
        respuesta_usuario = input("Escribe algo: ") # Obtener respuesta del usuario
        respuesta = Raw(load=respuesta_usuario) # Crear respuesta
        paquete_respuesta = paquete / respuesta # Crear paquete de respuesta
        sendp(paquete_respuesta) # Enviar paquete de respuesta

# ============================
# Menú Principal
# ============================
if __name__ == "__main__":
    print("Seleccione una opción:")
    print("1. Enviar mensaje")
    print("2. Enviar ping")
    print("3. Escanear puertos")
    print("4. Responder mensaje")
    print("5. Escanear red")
    print("6. Mostrar mensajes")
    print("7. Enviar mensaje desde máquina A")
    print("8. Responder mensaje desde máquina B")

    opcion = int(input("Ingrese el número de la opción deseada: "))

    if opcion == 1:
        mensaje = input("Ingrese el mensaje a enviar: ")
        enviar_mensaje(mensaje)
    elif opcion == 2:
        enviar_ping()
    elif opcion == 3:
        ip = input("Ingrese la IP a escanear: ")
        escanear_puertos(ip)
    elif opcion == 4:
        sniff(filter="udp", prn=responder_mensaje)
    elif opcion == 5:
        escanear_red()
    elif opcion == 6:
        sniff(filter="udp", prn=mostrar_mensaje)
    elif opcion == 7:
        mensaje = input("Ingrese el mensaje a enviar desde máquina A: ")
        enviar_mensaje_maquina_a(mensaje)
    elif opcion == 8:
        sniff(filter="udp", prn=responder_mensaje_maquina_b)
    else:
        print("Opción no válida.")

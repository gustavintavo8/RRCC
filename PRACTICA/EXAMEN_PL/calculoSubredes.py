import ipaddress
from math import ceil, log2

def calcular_subredes():
    try:
        # Paso 1: Ingresar la red inicial
        red_input = input("Introduce la red (e.g., 192.168.0.0/24): ")
        red = ipaddress.IPv4Network(red_input, strict=False)

        # Paso 2: Ingresar la cantidad de subredes necesarias
        num_subredes = int(input("Introduce la cantidad de subredes necesarias: "))

        # Paso 3: Ingresar los nombres y el número de hosts requeridos por subred
        subredes_datos = []
        for i in range(num_subredes):
            nombre = input(f"Introduce el nombre para la subred {i + 1}: ")
            hosts = int(input(f"Introduce el número de hosts para la subred {nombre}: "))
            subredes_datos.append((nombre, hosts))

        # Ordenar las subredes por número de hosts en orden descendente
        subredes_datos.sort(key=lambda x: x[1], reverse=True)

        # Calcular las subredes
        subredes_resultado = []
        direccion_actual = int(red.network_address)

        for nombre, hosts in subredes_datos:
            # Calcular el prefijo necesario para satisfacer el número de hosts
            prefijo = 32 - ceil(log2(hosts + 2))  # +2 para el broadcast y la dirección de red

            # Crear la subred consecutiva
            subred = ipaddress.IPv4Network((direccion_actual, prefijo), strict=False)
            subredes_resultado.append((nombre, subred))

            # Actualizar la dirección inicial para la siguiente subred
            direccion_actual = int(subred.broadcast_address) + 1

        # Generar la tabla de salida
        print("\nResultado:")
        print(f"{'Nombre':<25}{'Subred':<30}{'Primera IP':<25}{'Última IP':<25}{'Máscara':<20}{'Broadcast':<25}")
        for nombre, subred in subredes_resultado:
            # Asegurarse de que haya hosts disponibles en la subred
            hosts = list(subred.hosts())
            if len(hosts) > 0:
                primera_ip = hosts[0]
                ultima_ip = hosts[-1]
            else:
                primera_ip = "N/A"
                ultima_ip = "N/A"
            mascara = subred.netmask
            broadcast = subred.broadcast_address
            print(f"{nombre:<25}{str(subred):<30}{str(primera_ip):<25}{str(ultima_ip):<25}{str(mascara):<20}{str(broadcast):<25}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    calcular_subredes()
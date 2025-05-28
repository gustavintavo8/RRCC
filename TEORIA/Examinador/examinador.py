import json
import os
import unicodedata
import random

def cargar_preguntas(ruta):
    """Carga las preguntas desde un archivo JSON y limpia caracteres no validos."""
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            preguntas = json.load(archivo)
        return [limpiar_texto(pregunta) for pregunta in preguntas]
    except FileNotFoundError:
        print(f"No se encontró el archivo {ruta}. Verifica que exista en la misma carpeta que este script.")
        return []

def limpiar_texto(pregunta):
    """Limpia caracteres no validos de las preguntas y opciones."""
    for clave in pregunta:
        if isinstance(pregunta[clave], str):
            pregunta[clave] = unicodedata.normalize('NFKD', pregunta[clave]).encode('ascii', 'ignore').decode('utf-8')
        elif isinstance(pregunta[clave], list):
            pregunta[clave] = [unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('utf-8') for texto in pregunta[clave]]
    return pregunta

def presentar_pregunta(pregunta, numero):
    """Presenta una pregunta al usuario y devuelve el puntaje obtenido."""
    print(f"\nPregunta {numero}:")
    print(pregunta["pregunta"])
    for idx, opcion in enumerate(pregunta["opciones"], start=1):
        print(f"{idx}. {opcion}")
    
    respuesta_correcta = pregunta["opciones"].index(pregunta["respuesta_correcta"]) + 1
    comentario = pregunta.get("_comentario", "Sin comentario.")
    
    try:
        respuesta_usuario = int(input("Selecciona la opcion (1-4): "))
        if respuesta_usuario == respuesta_correcta:
            print("¡Correcto!")
            print(f"Comentario: {comentario}")
            return 1  # 1 punto por respuesta correcta
        else:
            print("Incorrecto.")
            print(f"La respuesta correcta era: {respuesta_correcta}. {pregunta['respuesta_correcta']}")
            print(f"Comentario: {comentario}")
            return -0.25  # -0.25 puntos por respuesta incorrecta
    except ValueError:
        print("Entrada no valida. Asegúrate de ingresar un número.")
        return 0  # Penalización por entrada inválida

def calcular_puntuacion(puntaje_total, total_preguntas):
    """Calcula la puntuacion en una escala de 0 a 5."""
    return round((puntaje_total / total_preguntas) * 5, 2)

def main():
    ruta_archivo = os.path.join(os.path.dirname(__file__), 'preguntas.json')
    preguntas = cargar_preguntas(ruta_archivo)
    
    if not preguntas:
        return

    print("\nOpciones:")
    print("1. Responder 25 preguntas aleatorias")
    print("2. Responder todas las preguntas")
    eleccion = input("Selecciona una opcion (1 o 2): ").strip()

    if eleccion == "1":
        preguntas = random.sample(preguntas, min(25, len(preguntas)))
    elif eleccion == "2":
        pass
    else:
        print("Opcion no valida. Cerrando el programa.")
        return

    print(f"\nSe han cargado {len(preguntas)} preguntas.")
    puntaje_total = 0
    
    for numero, pregunta in enumerate(preguntas, start=1):
        puntaje_total += presentar_pregunta(pregunta, numero)
    
    puntuacion_final = calcular_puntuacion(puntaje_total, len(preguntas))
    print(f"\nHas completado el examen. Puntaje total: {puntaje_total:.2f}/{len(preguntas)}")
    print(f"Puntuación en escala de 0 a 5: {puntuacion_final}")

if __name__ == "__main__":
    main()

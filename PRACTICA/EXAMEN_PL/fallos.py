# -*- coding: utf-8 -*-

# ============================
# Problemas Identificados
# ============================

# Problema 1: El PCA-1 está en otra red que no es la red A.
# - Descripción: El dispositivo PCA-1 no pertenece a la misma red que Router-A, lo que impide la comunicación directa.
# - Posible solución: Asegurarse de que PCA-1 tenga una dirección IP en la misma subred que Router-A, o configurar una ruta adecuada.

# Problema 2: Ruta estática en Router-A mal configurada.
# - Descripción: Router-A tiene una ruta estática configurada incorrectamente, lo que afecta el encaminamiento hacia las demás redes.
# - Posible solución: Revisar las rutas estáticas configuradas en Router-A y corregirlas para que apunten a las redes correctas con las interfaces adecuadas.

# Problema 3: Router-B no tiene ruta estática.
# - Descripción: Router-B carece de rutas estáticas hacia las redes conectadas a Router-A o al Servidor Web.
# - Posible solución: Configurar rutas estáticas en Router-B para garantizar que pueda alcanzar todas las redes necesarias.

# Problema 4: El Router-B tenía la misma IP en la interfaz 0/1 que el Router-A.
# - Descripción: Una configuración errónea asignó la misma dirección IP a Router-A y Router-B en sus interfaces respectivas.
# - Posible solución: Cambiar la dirección IP de una de las interfaces para garantizar que no haya conflictos en la red.

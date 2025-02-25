import time # importamos la libreria time, que tiene funciones para manejar el tiempo en Python.
import schedule # importamos la libreria schedule, que permite programar tareas automáticas.
from plyer import notification # importamos la función notification de la librería plyer. Plyer es una librería en Python que permite enviar notificaciones en Windows, macOS y Linux.

def enviar_notificacion(): # definimos una función de enviar notificación
    notification.notify( # llamamos a la función notify() que crea una notificación emergente
        title="Recordatorio", # definimos el título de la notificación 
        message="¡No olvides hacer una pausa y estirarte!", # definimos el mensaje de la notificación
        timeout= 8  # definimos el tiempo que se muestra la notificación a 8 segundos
    )

schedule.every(1).minute.do(enviar_notificacion) # programamos la función enviar_notificacion() para que se ejecute cada 1 minuto.

try: # iniciamos un bucle infinito para ejecutar las tareas programadas de forma continua
    while True: 
        schedule.run_pending() # ejecuta las tareas programadas que estén pendientes  
        time.sleep(60)  # espera 60 segundos antes de revisar nuevamente, pausa la ejecución del programa por un tiempo determinado.
except KeyboardInterrupt: # captura la interrupción del usuario (Ctrl + C)  
    print("\nPrograma detenido por el usuario.") # mensaje de salida cuando el usuario detiene el programa 


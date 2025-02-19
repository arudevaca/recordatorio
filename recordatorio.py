import time # time tiene funciones para manejar el tiempo en Python.
import schedule # Permite programar tareas automáticas.
from plyer import notification # Importa la función notification de la librería plyer. Plyer es una librería en Python que permite enviar notificaciones en Windows, macOS y Linux.

def enviar_notificacion():
    notification.notify( # Llama a la función notify() que crea una notificación emergente en el sistema operativo.
        title="Recordatorio", # Define el título de la notificación 
        message="¡No olvides hacer una pausa y estirarte!", # Define el mensaje de la notificación
        timeout= 8  # La notificación se muestra durante 8 segundos
    )

schedule.every(1).hours.do(enviar_notificacion) # Programa la función enviar_notificacion() para que se ejecute cada 1 hora.

try:
    while True:
        schedule.run_pending()
        time.sleep(60)  # Esperar 60 segundos antes de revisar nuevamente, pausa la ejecución del programa por un tiempo determinado.
except KeyboardInterrupt:
    print("\nPrograma detenido por el usuario.")


Recordatorio Automático
Este proyecto es un script en Python que muestra notificaciones emergentes automáticas cada minuto para recordarte hacer una pausa y estirarte. Utiliza la librería schedule para programar las notificaciones y plyer para mostrarlas en pantalla.

Características
Envía notificaciones emergentes cada minuto.
Se ejecuta de forma continua hasta que el usuario lo detenga manualmente.
Código simple y fácil de modificar para personalizar los tiempos de recordatorio.

Requisitos
Asegúrate de tener instalado Python 3 en tu sistema. 
También necesitarás las librerías schedule y plyer, que puedes instalar con:
pip install schedule plyer

Instalación y Uso
Clona este repositorio o descarga los archivos.
git clone https://github.com/arudevaca/recordatorio.git
Navega hasta la carpeta del proyecto.
cd recordatorio
Ejecuta el script.
python recordatorio.py

Para detener el programa, presiona Ctrl + C en la terminal.

Personalización
Si deseas cambiar la frecuencia de los recordatorios, edita el archivo recordatorio.py y modifica la programación de schedule.every(1).minute.do(enviar_notificacion), ajustando la unidad de tiempo según sea necesario (hours, seconds, etc.).

Contribución
Si deseas mejorar este proyecto, ¡eres bienvenido/a a contribuir! Puedes hacer un fork, modificarlo y enviar un pull request.

Licencia
Este proyecto está bajo la licencia MIT.

# CookieBot
Una herramienta de automatización para jugar **Cookie Clicker**.

## Características
- Clics automáticos
- Compra de mejoras
- Registro de rendimiento

## Tecnologías Utilizadas
- Python
- Selenium
- SQLite

## Instrucciones de Uso
1. Clona el repositorio.
2. Instala las dependencias requeridas.
3. Ejecuta el script `main.py`.

## Funcionamiento de la Base de Datos
Los datos sobre el rendimiento del juego se guardan en una base de datos llamada `cookie_clicker.db`. La conexión a esta base de datos se establece al inicio del programa, pero **los registros no se efectúan hasta que han pasado 5 minutos de ejecución**. Esto se hace para asegurar que la información recopilada es significativa y que se han realizado suficientes interacciones en el juego, lo que permite un análisis más preciso del rendimiento a lo largo del tiempo.

Esto asegura que la base de datos no se llene de datos irrelevantes o incompletos, y que los resultados reflejen el rendimiento real del bot durante un periodo sostenido.

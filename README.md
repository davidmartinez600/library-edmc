Sistema de Gestión de Biblioteca
Este es un proyecto de gestión de biblioteca completo, desarrollado con Django. Incluye un backend robusto, una API RESTful para la manipulación de datos y una interfaz de usuario intuitiva construida con Bootstrap 4.

🚀 Configuración Local
Sigue estos pasos para poner en marcha el proyecto en tu máquina local:

Clonar el Repositorio:

Bash

git clone https://github.com/davidmartinez600/library-edmc.git
cd library-edmc
Configurar el Entorno de Desarrollo:

Bash

python -m venv venv
source venv/bin/activate  # En Windows, usa `venv\Scripts\activate`
pip install -r requirements.txt
Configurar Variables de Entorno:
Crea un archivo .env en la raíz del proyecto y añade las siguientes variables. Para la base de datos local, se usa SQLite.

SECRET_KEY=tu_clave_secreta_aqui
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
Ejecutar la Aplicación:

Bash

python manage.py migrate
python manage.py runserver
La aplicación estará disponible en http://127.0.0.1:8000/.

🌐 Despliegue en Producción
El proyecto está desplegado en Render.com. Ten en cuenta que la primera carga puede demorar un poco, ya que el servidor de la base de datos puede estar inactivo si no se ha utilizado recientemente.

URL de la aplicación: https://library-edmc.onrender.com

🔑 Credenciales de Acceso
Puedes utilizar estas credenciales para probar la aplicación en el entorno de producción:

Super usuario:

Usuario: library

Contraseña: 1234

Usuario regular:

Usuario: david

Contraseña: Library123$

# Sistema de Gestión de Biblioteca

Este es un proyecto de gestión de biblioteca desarrollado con Django, que incluye un backend, una API RESTful y una interfaz de usuario con Bootstrap 4.

## Configuración Local

Sigue estos pasos para ejecutar el proyecto en tu máquina:

1. Clona el repositorio y accede:
```bash
git clone https://github.com/davidmartinez600/library-edmc
cd library-edmc
````

2. Configura el entorno de desarrollo:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Configurar variables de entorno - Crea un archivo `.env` en la raíz del proyecto. Para la base de datos local, puedes usar SQLite.

```env
SECRET_KEY=tu_clave_secreta_aqui
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

4. Ejecuta la aplicación:

```bash
python manage.py migrate
python manage.py runserver
```

La aplicación estará disponible en [http://127.0.0.1:8000](http://127.0.0.1:8000/).

## Despliegue en Producción

El proyecto está desplegado en Render.com. Ten en cuenta que la primera carga puede demorar un poco porque el servidor de la base de datos de Render.com puede estar inactivo si no se ha usado recientemente.

**URL de la aplicación:**
[https://library-edmc.onrender.com](https://library-edmc.onrender.com)

## Credenciales de Acceso

Puedes usar estas credenciales para probar la aplicación en producción.

**Super usuario:**
`library` / `1234`

**Usuario regular:**
`david` / `Library123$`

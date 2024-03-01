# app_rastreo
Aplicación web donde se administra una flotilla de vehículos y se pueda ver su posición.

## Instalación

1. Clona este repositorio en tu máquina local.
2. Navegue hasta el directorio del proyecto.

### Configuración del entorno virtual

Cree y active un entorno virtual para gestionar las dependencias del proyecto.

```golpecito
python -m virtualenv venv # Crear entorno virtual
source venv/bin/activate # Activar entorno virtual (Linux/Mac)
venv\Scripts\activate # Activar entorno virtual (Windows)
Nota: si no tiene instalado virtualenv entonces instalar con pip: pip install virtualenv
```

### Instalar dependencias

Instale las dependencias requeridas desde `requirements.txt`.

```bash
pip install -r requirements.txt
```

## Uso

### Ejecutando la aplicación Flask

Inicie el servidor de desarrollo de Flask para ejecutar la API.

```bash
python app.py
```

Se podrá acceder a la API en `http://localhost:5000`.

### Ejecución de pruebas unitarias

Ejecute pruebas unitarias utilizando el conjunto de pruebas proporcionado.

```bash
python unit_test.py
```

## Puntos finales

- `POST /api/vehicles`: Agregar un nuevo vehículo.
- `PUT /api/vehicles/<vehicle_id>`: Actualiza un vehículo existente.
- `DELETE /api/vehicles/<vehicle_id>`: Elimina un vehículo.
- `GET /api/vehicles`: Obtiene todos los vehículos.

## Autenticación

La API utiliza autenticación básica HTTP. Utilice las siguientes credenciales:

- Nombre de usuario: `admin`
- Contraseña: `123123`

## Contribuyendo

¡Las contribuciones son bienvenidas! No dude en enviar cualquier problema o solicitud de extracción.

## Licencia

Este proyecto tiene la licencia [Licencia MIT] (LICENCIA).

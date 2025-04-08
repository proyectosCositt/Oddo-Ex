# Entorno de Desarrollo Odoo

Este es un entorno de desarrollo para crear módulos personalizados de Odoo utilizando Docker, con soporte para importación y exportación de datos.

## Requisitos

- Docker
- Docker Compose
- Python 3.6 o superior (para los scripts de importación/exportación)

## Guía de inicio rápido desde cero

### 1. Configuración inicial

1. Clona este repositorio o copia estos archivos a tu directorio de trabajo.

2. Inicia el entorno por primera vez:

```bash
docker-compose up -d
```

3. Si deseas reiniciar todo desde cero (eliminar base de datos y volúmenes):

```bash
docker-compose down -v
docker-compose up -d
```

### 2. Creación de la base de datos

1. Accede a Odoo desde tu navegador:
   - URL: http://localhost:8069
   
2. En la pantalla de bienvenida, crea una nueva base de datos:
   - Nombre de la base de datos: mi_base_datos (o el que prefieras)
   - Correo electrónico: admin (o tu correo)
   - Contraseña: admin (usa una contraseña segura en entornos de producción)
   - Idioma: Español (o el que prefieras)
   - País: España (o el que prefieras)
   
3. Haz clic en "Crear base de datos"

Alternativamente, puedes crear la base de datos desde la línea de comandos:

```bash
docker-compose exec web odoo --stop-after-init -i base -d mi_base_datos --db_host=db --db_user=odoo --db_password=odoo
```

### 3. Desarrollo de módulos

Para crear un nuevo módulo:

1. Crea una carpeta con el nombre de tu módulo en el directorio `addons/`:

```bash
mkdir -p addons/mi_modulo/models addons/mi_modulo/views addons/mi_modulo/security
```

2. Estructura básica del módulo:
   ```
   mi_modulo/
   ├── __init__.py           # Importa los submódulos
   ├── __manifest__.py       # Metadatos del módulo
   ├── models/               # Modelos de datos
   │   ├── __init__.py
   │   └── models.py
   ├── views/                # Vistas XML
   │   └── views.xml
   ├── security/            # Reglas de seguridad
   │   └── ir.model.access.csv
   ```

3. Actualiza la lista de aplicaciones en Odoo:
   - Activa el modo desarrollador (Configuración → Activar el modo desarrollador)
   - Ve a Aplicaciones → Actualizar lista de aplicaciones
   - Busca tu módulo e instálalo

### 4. Importación y exportación de datos

Este entorno incluye scripts para facilitar la importación y consulta de datos en Odoo.

#### 4.1. Preparar un archivo CSV para importación

Crea un archivo CSV con las columnas correspondientes a los campos que deseas importar. Ejemplo (`datos_ejemplo.csv`):

```csv
nombre,email,telefono,calle,ciudad,es_empresa
Empresa ABC,contacto@empresaabc.com,+34 912345678,"Calle Principal 123","Madrid",1
Juan Pérez,juan.perez@ejemplo.com,+34 611223344,"Avda. de la Constitución 45","Barcelona",0
```

#### 4.2. Importar datos desde CSV

```bash
cd scripts
python import_data.py datos_ejemplo.csv
```

El script está configurado para importar contactos, pero puede modificarse para cualquier modelo de Odoo.

#### 4.3. Consultar datos importados

```bash
cd scripts
python consultar_datos.py res.partner
```

## Estructura del proyecto

- `docker-compose.yml`: Configuración de los contenedores Docker
- `config/`: Archivos de configuración de Odoo
  - `odoo.conf`: Configuración principal de Odoo
- `addons/`: Módulos personalizados de Odoo
  - `mi_modulo/`: Módulo de ejemplo
- `scripts/`: Scripts para importación y consulta de datos
  - `import_data.py`: Importación de datos desde CSV
  - `consultar_datos.py`: Consulta de datos mediante la API de Odoo
  - `datos_ejemplo.csv`: Ejemplo de archivo CSV para importación

## Comandos útiles

- Iniciar el entorno: `docker-compose up -d`
- Ver logs: `docker-compose logs -f`
- Detener el entorno: `docker-compose down`
- Reiniciar Odoo: `docker-compose restart web`
- Eliminar todo y comenzar desde cero: `docker-compose down -v`

## Solución de problemas

### No puedo conectarme a Odoo
- Verifica que los contenedores estén en ejecución: `docker-compose ps`
- Revisa los logs para ver si hay errores: `docker-compose logs -f web`

### Error al importar datos
- Verifica que la estructura del CSV coincida con los campos mapeados en el script
- Comprueba que la base de datos existe y las credenciales son correctas
- Para campos relacionales (many2one), debes proporcionar el ID correcto 
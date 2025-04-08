# Entorno de Desarrollo Odoo

Este es un entorno de desarrollo para crear módulos personalizados de Odoo utilizando Docker.

## Requisitos

- Docker
- Docker Compose

## Instrucciones de uso

1. Inicia el entorno:

```bash
docker-compose up -d
```

2. Accede a Odoo desde tu navegador:
   - URL: http://localhost:8069
   - Para la primera instalación, usa la contraseña de administrador: admin

3. Estructura del proyecto:
   - `addons/`: Directorio donde crear tus módulos personalizados
   - `config/`: Archivos de configuración de Odoo

## Desarrollo de módulos

Para crear un nuevo módulo:

1. Crea una carpeta con el nombre de tu módulo en el directorio `addons/`
2. Estructura básica del módulo:
   ```
   mi_modulo/
   ├── __init__.py
   ├── __manifest__.py
   ├── models/
   │   ├── __init__.py
   │   └── models.py
   ├── views/
   │   └── views.xml
   ├── security/
   │   └── ir.model.access.csv
   └── static/
       ├── description/
       │   └── icon.png
       └── src/
   ```

3. Actualiza la lista de aplicaciones en Odoo y busca tu módulo para instalarlo.

## Comandos útiles

- Ver logs: `docker-compose logs -f`
- Detener el entorno: `docker-compose down`
- Reiniciar Odoo: `docker-compose restart web` 
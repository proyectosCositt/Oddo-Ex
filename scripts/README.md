# Scripts para Gestión de Datos en Odoo

Esta carpeta contiene scripts para facilitar la importación y consulta de datos en Odoo a través de la API XML-RPC.

## Requisitos

- Python 3.6 o superior
- Odoo funcionando en Docker (según la configuración del proyecto principal)
- Base de datos "mi_base_datos" ya creada en Odoo

## Scripts disponibles

### 1. Importación de datos desde CSV (`import_data.py`)

Este script permite importar datos desde un archivo CSV a un modelo de Odoo.

```bash
python import_data.py datos_ejemplo.csv
```

El script está configurado para importar contactos (modelo `res.partner`) pero puede ser modificado para importar cualquier tipo de datos.

### 2. Consulta de datos (`consultar_datos.py`)

Este script permite consultar datos de cualquier modelo de Odoo.

```bash
python consultar_datos.py res.partner
```

Si no se especifica un modelo, consulta los contactos por defecto.

## Estructura de los archivos CSV

Los archivos CSV deben tener una estructura específica según el modelo al que se van a importar los datos. El archivo `datos_ejemplo.csv` muestra un ejemplo para el modelo `res.partner` (contactos).

## Personalización

Para importar datos a otros modelos, debes modificar el mapeo de campos en el script `import_data.py`:

```python
# Ejemplo para otro modelo (por ejemplo, productos)
campos_mapeados = {
    'codigo': 'default_code',
    'nombre': 'name',
    'precio': 'list_price',
    'categoria': 'categ_id'
}

importar_datos_desde_csv(archivo_csv, 'product.template', campos_mapeados)
```

## Errores comunes

- **Error de autenticación**: Verifica que las credenciales (usuario/contraseña) sean correctas
- **Error al crear registros**: Asegúrate de que los campos mapeados existan en el modelo y que los datos tengan el formato correcto
- **Campos relacionales**: Para campos Many2one (como country_id), debes proporcionar el ID o usar una función de búsqueda 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xmlrpc.client
import csv
import sys
import os

# Configuración de conexión a Odoo
url = 'http://localhost:8069'
db = 'mi_base_datos'  # Nombre de la base de datos
username = 'admin'  # Usuario administrador
password = 'admin'  # Contraseña (ajustar según la configurada)

# Función principal para importar datos desde un CSV a Odoo
def importar_datos_desde_csv(archivo_csv, modelo_odoo, campos_mapeados):
    """
    Importa datos desde un archivo CSV a un modelo de Odoo.
    
    Args:
        archivo_csv: Ruta al archivo CSV con los datos
        modelo_odoo: Nombre del modelo de Odoo (ej: 'res.partner')
        campos_mapeados: Diccionario que mapea las columnas del CSV a los campos de Odoo
                        ej: {'nombre_csv': 'name', 'correo_csv': 'email'}
    """
    try:
        # Conectar con Odoo
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        uid = common.authenticate(db, username, password, {})
        
        if not uid:
            print("Error de autenticación. Verifica las credenciales.")
            return False
        
        # Crear proxy para llamar a métodos del modelo
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        
        # Leer el archivo CSV
        with open(archivo_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            registros_creados = 0
            
            for fila in reader:
                # Preparar datos según el mapeo
                valores = {}
                for campo_csv, campo_odoo in campos_mapeados.items():
                    if campo_csv in fila:
                        valores[campo_odoo] = fila[campo_csv]
                
                # Crear registro en Odoo
                try:
                    nuevo_id = models.execute_kw(db, uid, password, 
                                            modelo_odoo, 'create', 
                                            [valores])
                    registros_creados += 1
                    print(f"Registro creado con ID: {nuevo_id}")
                except Exception as e:
                    print(f"Error al crear registro: {str(e)}")
                    print(f"Datos: {valores}")
            
            print(f"Importación completada. {registros_creados} registros creados.")
            return True
    
    except Exception as e:
        print(f"Error general: {str(e)}")
        return False

# Ejemplo de uso
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python import_data.py [archivo_csv]")
        sys.exit(1)
    
    archivo_csv = sys.argv[1]
    
    if not os.path.exists(archivo_csv):
        print(f"El archivo {archivo_csv} no existe.")
        sys.exit(1)
    
    # Ejemplo para importar contactos (res.partner)
    campos_mapeados = {
        'nombre': 'name',
        'email': 'email',
        'telefono': 'phone',
        'calle': 'street',
        'ciudad': 'city',
        'pais': 'country_id',
        'es_empresa': 'is_company'
    }
    
    importar_datos_desde_csv(archivo_csv, 'res.partner', campos_mapeados) 
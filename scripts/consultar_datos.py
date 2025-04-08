#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xmlrpc.client
import sys

# Configuración de conexión a Odoo
url = 'http://localhost:8069'
db = 'mi_base_datos'  # Nombre de la base de datos
username = 'admin'  # Usuario administrador
password = 'admin'  # Contraseña (ajustar según la configurada)

def consultar_datos(modelo, campos=None, dominio=None, limite=None):
    """
    Consulta datos en Odoo mediante la API XML-RPC.
    
    Args:
        modelo: Nombre del modelo de Odoo (ej: 'res.partner')
        campos: Lista de campos a recuperar (None para todos)
        dominio: Filtro de búsqueda en formato lista de Odoo
        limite: Número máximo de registros a recuperar
        
    Returns:
        Lista de registros encontrados
    """
    try:
        # Autenticación
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        uid = common.authenticate(db, username, password, {})
        
        if not uid:
            print("Error de autenticación. Verifica las credenciales.")
            return False
        
        # Crear proxy para llamar a métodos del modelo
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        
        # Configurar parámetros
        if campos is None:
            campos = []  # Recuperará todos los campos
        if dominio is None:
            dominio = []  # Sin filtros
        
        # Opciones de búsqueda
        options = {}
        if limite:
            options['limit'] = limite
            
        # Buscar IDs
        ids = models.execute_kw(db, uid, password,
                          modelo, 'search',
                          [dominio], options)
        
        if not ids:
            print(f"No se encontraron registros para {modelo} con el filtro {dominio}")
            return []
            
        # Leer registros
        registros = models.execute_kw(db, uid, password,
                                 modelo, 'read',
                                 [ids, campos])
        
        return registros
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    # Por defecto consulta contactos
    modelo = 'res.partner'
    if len(sys.argv) > 1:
        modelo = sys.argv[1]
    
    print(f"Consultando registros de {modelo}...")
    registros = consultar_datos(modelo, limite=10)
    
    if registros:
        print(f"Se encontraron {len(registros)} registros:")
        for reg in registros:
            print(f"ID: {reg['id']}, Nombre: {reg.get('name', 'Sin nombre')}")
            for k, v in reg.items():
                if k not in ['id', 'name']:
                    print(f"  - {k}: {v}")
            print("-" * 40) 
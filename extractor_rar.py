#pip install patool

import patoolib
#Setting the route
import os
from pathlib import Path
import tensorflow
 
 
def new_route(route_file):
    base_route = Path.home()
    complete_route = os.path.join(base_route, route_file)
    return complete_route
all_routes = new_route("Downloads\Imports_Unit_Report_DPW.rar")
print(all_routes)
 
def new_route_destino(route_file):
    base_route = Path.home()
    complete_route = os.path.join(base_route, route_file)
    return complete_route
destino_ruta = new_route("Downloads")
 
def descomprimir_rar(archivo_rar, destino):
    # Verificar si el archivo rar existe
    if not os.path.isfile(archivo_rar):
        raise FileNotFoundError(f"El archivo {archivo_rar} no existe.")
   
    # Crear el directorio de destino si no existe
    if not os.path.isdir(destino):
        os.makedirs(destino)
   
    # Descomprimir el archivo rar
    try:
        patoolib.extract_archive(archivo_rar, outdir=destino)
        print(f"Archivos extraídos en {destino}")
    except Exception as e:
        print(f"Ocurrió un error al descomprimir el archivo RAR: {e}")
 
# Ejemplo de uso
archivo_rar = all_routes
destino = destino_ruta
descomprimir_rar(archivo_rar, destino)
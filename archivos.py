from skimage import io, img_as_ubyte
from pathlib import Path
import requests
import json
import os
import time
directorio_actual = Path.cwd()

def armar_ruta(nombre):
  return (directorio_actual / 'imagenes' / nombre).resolve()#devuelve una ruta prara NOMBRE

def leer_imagen(nombre):
  return io.imread(armar_ruta(nombre))#devuelve la ruta de rutas Leible

def escribir_imagen(nombre, imagen):
  io.imsave(armar_ruta(nombre), img_as_ubyte(imagen))#nombra una imagen y la guarda


######################copiado  de la clase anterior#############################################
class Pixabay():
  def __init__(self, key, carpeta_imagenes):
    self.key = key
    self.carpeta_imagenes = carpeta_imagenes
    self.nombres=[]
    

  def buscar_imagenes(self, query, cantidad):
    #utiliso un url de pixabay
    url = f'https://pixabay.com/api/?key={self.key}&per_page={cantidad}&q={query}&image_type=photo&lang=es'
    response = requests.get(url)
    jsonResponse = json.loads(response.text)
    return map(lambda h: h['largeImageURL'], jsonResponse['hits'])
    #lista de rutas
  
  def descargar_imagen(self, url,leer_imagenes):
    
    bytes_imagen = requests.get(url)
    nombre_imagen = url.split('/')[-1]
    ruta_archivo = os.path.join(self.carpeta_imagenes, nombre_imagen)
    with open(ruta_archivo, 'wb') as archivo:
      archivo.write(bytes_imagen.content)
    self.nombres.append(leer_imagenes(nombre_imagen))
    
     
    



  #debo guardar la ruta en cuanto la descargo

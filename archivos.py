import os
# import cv2
# import numpy as np
from PIL import Image
from skimage import io
import requests
import json

# carpeta_imagenes = './imagenes'
carpeta_imagenes = '/home/sebas/UNaHur/progConcu_2020verano/python-manipulacion-imagenes/imagenes'

def armar_ruta(nombre):
  return os.path.join(carpeta_imagenes, nombre)

def leer_imagen(nombre):
  return Image.open(armar_ruta(nombre))

def escribir_imagen(nombre, imagen):
  Image.fromarray(imagen).save(armar_ruta(nombre))
  #esto lo guarda

def leer_imagen2(nombre):
  return io.imread(armar_ruta(nombre))

def escribir_imagen2(nombre, imagen):
  io.imsave(armar_ruta(nombre),imagen)


######################copiado  de la clase anterior#############################################
class Pixabay():
  def __init__(self, key, carpeta_imagenes):
    self.key = key
    self.carpeta_imagenes = carpeta_imagenes
    

  def buscar_imagenes(self, query, cantidad):
    #utiliso un url de pixabay
    url = f'https://pixabay.com/api/?key={self.key}&per_page={cantidad}&q={query}&image_type=photo&lang=es'
    response = requests.get(url)
    jsonResponse = json.loads(response.text)
    return map(lambda h: h['largeImageURL'], jsonResponse['hits'])
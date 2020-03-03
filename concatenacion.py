import cv2
from archivos import leer_imagen, escribir_imagen,Pixabay
import logging
import threading
import time
imagenes=[]
api=Pixabay('15336424-3010f778fbb10add8cf653c86',"./imagenes")
#monitor=threading.Condition()

def concatenar_horizontal(imagenes):
  # Buscamos el alto menor entre todas las imágenes
  alto_minimo = min(im.shape[0] for im in imagenes)

  # Redimensionamos las imágenes para que tengan todas el mismo alto
  imagenes_redimensionadas = [cv2.resize(im, (int(im.shape[1] * alto_minimo / im.shape[0]), alto_minimo))
                    for im in imagenes]

  # Concatenamos
  return cv2.hconcat(imagenes_redimensionadas)

def concatenar_vertical(imagenes):
  # Buscamos el ancho menor entre todas las imágenes
  ancho_minimo = min(im.shape[1] for im in imagenes)

  # Redimensionamos las imágenes para que tengan todas el mismo ancho
  imagenes_redimensionadas = [cv2.resize(im, (ancho_minimo, int(im.shape[0] * ancho_minimo / im.shape[1])))for im in imagenes]

  # Concatenamos
  return cv2.vconcat(imagenes_redimensionadas)

urls = api.buscar_imagenes("cosas", 5)#es una lista de hits

for u in urls:
  logging.info(f'Descargando {u}')
  threading.Thread(target=api.descargar_imagen, args=[u]).start()
  #monitor.notify()
if len(api.nombres)>imagenes:
  for i in range(2):
    imagenes.append(leer_imagen(api.nombres.pop(0)))

  
escribir_imagen('concatenada-vertical.jpg', concatenar_vertical(imagenes))    
escribir_imagen('concatenada-horizontal.jpg', concatenar_horizontal(imagenes))  
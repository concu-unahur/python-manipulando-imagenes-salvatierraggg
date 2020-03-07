
import cv2
from archivos import leer_imagen, escribir_imagen,Pixabay
import logging
import threading
import time
imagenesDisponibles=threading.Condition()
paresDisponibles=threading.Condition()
logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
i=0
imagenes=[]
api=Pixabay('15336424-3010f778fbb10add8cf653c86',"./imagenes")


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

logging.info('buscando imagenes')

urls = api.buscar_imagenes("cosas",8)#es una lista de hits

logging.info('iniciando descargas')

for u in urls:
  i+=1
  with imagenesDisponibles:
    try:
      logging.info(f'Descargando {u}')
      api.descargar_imagen(u,f"{i}.jpg")
      #threading.Thread(target=api.descargar_imagen, args=[u,f"{i}.jpg"]).start()
    finally:
      time.sleep(2)
      if len(api.nombres)>=2:
        with paresDisponibles:
          imagenes.append([leer_imagen(api.nombres.pop(0)),leer_imagen(api.nombres.pop(0))])
          logging.info("notificando")
          paresDisponibles.notify()


j=0
while (True):
    with paresDisponibles:
      while len(imagenes)<j+1:
        paresDisponibles.wait()
      logging.info("termina una espera")
      threading.Thread(target=escribir_imagen,args=[f'concatenada-vertical{j+1}.jpg', concatenar_vertical(imagenes[j])]).start()
      threading.Thread(target=escribir_imagen,args=[f'concatenada-horizontal{j+1}.jpg', concatenar_horizontal(imagenes[j])]).start()

      #escribir_imagen(f'concatenada-vertical{j+1}.jpg',concatenar_vertical(imagenes[j]))
      #escribir_imagen(f'concatenada-horizontal{j+1}.jpg',concatenar_horizontal(imagenes[j]))
      j+=1

    

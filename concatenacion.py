import numpy as np
from PIL import Image
from archivos import *




def concatenar_horizontal(imagenes):#imagenes es una lista de imagenes
  min_img_shape = sorted([(np.sum(i.size), i.size) for i in imagenes])[0][1]
  
  return np.hstack(list((np.asarray(i.resize(min_img_shape, Image.ANTIALIAS)) for i in imagenes)))

def concatenar_vertical(imagenes):
  min_img_shape = sorted([(np.sum(i.size), i.size) for i in imagenes])[0][1]
  return np.vstack(list((np.asarray(i.resize(min_img_shape, Image.ANTIALIAS)) for i in imagenes)))





##########################
privado=Pixabay('15336424-3010f778fbb10add8cf653c86', "./imagenes")#mi clave y donde guardar
urls=privado.buscar_imagenes("LOL", 20)
##########################



imagenes=[]
for u in urls:
  imagenes.append(leer_imagen(u))

imagen1 = leer_imagen('1.jpg')
imagen2 = leer_imagen('2.jpg')

escribir_imagen('concatenada-vertical.jpg', concatenar_vertical(imagenes))    
escribir_imagen('concatenada-horizontal.jpg', concatenar_horizontal(imagenes))    

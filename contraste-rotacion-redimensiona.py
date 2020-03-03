from archivos import leer_imagen, escribir_imagen
from skimage import exposure, transform, io


def contraste_adaptativo(img):
  # Contraste adaptativo: https://en.wikipedia.org/wiki/Adaptive_histogram_equalization
  return exposure.equalize_adapthist(img, clip_limit=0.03)

def rotacion(img, angulo):
  return transform.rotate(img, angulo)

def redimensionar(img, ancho, alto):
  return transform.resize(img, (ancho, alto))

imagen1 = leer_imagen('1.jpg')

escribir_imagen('contraste.jpg', contraste_adaptativo(imagen1))
escribir_imagen('rotacion.jpg', rotacion(imagen1, 25))
escribir_imagen('redimensionada.jpg', redimensionar(imagen1, 500, 500))
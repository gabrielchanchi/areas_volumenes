import math
def calcular_area_cuadrado (lado):
	area=lado*lado
	return area

def calcular_volumen_paralelepipedo(base,altura, alto):
	volumen=base*altura*alto
	return volumen

def calcular_volumen_esfera(radio)
	area=(4/3)*math.pi*radio**3
	return volumen
	 
def calular_area_rombo (diagonal,diagonal1 ):
 	area=((diagonal*diagonal1)/2)
 	return area

def calcular_volumen_cubo(lado):

 	volumen=lado**3
	return volumen

def teorema_Heron(l1, l2, l3):
	perimetro=(l1+l2+l3)/2
	area=(perimetro*(perimetro-l1)*(perimetro-l2)*(perimetro-l3))**(1/2)
	return area

def calcular_volumen_cilindro(radio,altura):
	volumenc=math.pi*radio**2*altura
	return volumenc
	 
def calcular_area_trapecio(base, altura, superior):
	area=((base+superior)*altura)/2
 	return area

def calcular_area_esfera (radio):
 	area= math.pi*radio**2
	return area

def area_circulo(R):
  area=math.pi*R**2
  return area

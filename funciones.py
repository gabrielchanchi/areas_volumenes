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
	 
def calular_area_rombo (Diagonal,diagonal1 ):
	area=((Diagonal*diagonal1)/2)
	return area

def calcular_volumen_cubo(lado):
 	volumen=lado**3
	return volumen












def teorema_Heron(l1, l2, l3):
    perimetro=(l1+l2+l3)/2
    area=(perimetro*(perimetro-l1)*(perimetro-l2)*(perimetro-l3))**(1/2)
    return area

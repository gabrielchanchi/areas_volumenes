def calcular_area_cuadrado (lado):
	area=lado*lado
	return area

def calcular_volumen_paralelepipedo(base,altura, alto):
	volumen=base*altura*alto
	return volumen

def calular_area_rombo (Diagonal,diagonal1 ):
	area=((Diagonal*diagonal1)/2)
	return area

def calcular_volumen_cubo(lado):
 	volumen=lado**3
	return volumen
	
#print(f"El volumen de un cilindro es {calcular_volumen_cilindro(4)}")
def calcular_volumen_cilindro(radio,altura):
	volumenc=math.pi*radio**2*altura
	return volumenc
	 
	

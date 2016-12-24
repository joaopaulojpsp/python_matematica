# Conjuntos dos numeros inteiros Z

def numeros_inteiros():
	print("Numeros inteiros(Z): ")
	z = -14;
	print("...")
	while(z < 15):
		print(z)
		z = z + 1
	print("...")
	
def numeros_inteiros_positivos():
	print("Numeros Inteiros Positivos(Z+): ")
	z = 0;
	while(z < 15):
		print(z)
		z = z + 1
	print("...")
	
def numeros_inteiros_negativos():
	print("Numeros Inteiros Negativos(Z-): ")
	z = -14;
	print("...")
	while(z < 1):
		print(z)
		z = z + 1
	print("...")

def numeros_inteiros_positivos_sem_zero():
	print("Numeros Inteiros Positivos sem o zero(Z*+): ")
	z = 1;
	while(z < 15):
		print(z)
		z = z + 1
	print("...")
	
numeros_inteiros_positivos_sem_zero()
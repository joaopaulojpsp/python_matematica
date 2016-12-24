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
	
def numeros_inteiros_negativos_sem_zero():
	print("Numeros Inteiros Negativos Sem o Zero(Z*-): ")
	z = -14;
	print("...")
	while(z < 0):
		print(z)
		z = z + 1

def options():
	print("Digite um numero: ")
	print("1- Todos os Numeros Inteiros (Z)")
	print("2- Todos os Numeros Inteiros Positivos (Z+)")
	print("3- Todos os Numeros Inteiros  Negativos (Z-)")
	print("4- Todos os Numeros Inteiros Positivos Sem o Zero (Z*+)")
	print("5- Todos os Numeros Inteiros Negativos Sem o Zero (Z*-)")
	print("6- Para Sair")
	option = input()
	return option

option = 7
while(option != 6):
	if(option == 1):
		numeros_inteiros()
	elif(option == 2):
		numeros_inteiros_positivos()
	elif(option == 3):
		numeros_inteiros_negativos()
	elif(option == 4):
		numeros_inteiros_positivos_sem_zero()
	elif(option == 5):
		numeros_inteiros_negativos_sem_zero()
	
	
	option = options()

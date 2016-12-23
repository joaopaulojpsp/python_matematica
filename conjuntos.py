# Conjuntos

# Conjuntos dos numeros naturais
def naturais_sem_zero():
	n = 1
	print("Conjuntos do N(Naturais sem Zero)")
	while(n < 15):
		print(n)
		n = n + 1

		
#--------------------------------------------
		
# Conjuntos dos numeros naturais
def naturais_com_zero():
	n = 0	
	print("Conjuntos do N*(Naturais com Zero)")
	while(n < 15):
		print(n)
		n = n + 1
	
print("1 para naturaiz sem o 0")
print("0 para naturaiz com o 0")
option = input()
if(option == 1):
	naturais_sem_zero()
elif(option == 0):
	naturais_com_zero()


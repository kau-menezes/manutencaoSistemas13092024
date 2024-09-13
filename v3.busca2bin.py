# Base-de-algoritmos-em-C-v3 /busca2bin.c

vet = []
busca = 0
cont = 0 
medio = 0 
alto = 0
baixo = 0
achou = 0

for i in range(10):
    vet.append(int(input(f"Digite o valor do {i + 1} número: ")))
    
vet.sort()
    
busca = int(input("Digite um valor a ser procurado: "))

achou = 0
baixo = 0
alto = 9

while baixo <= alto and achou == 0:
    
    if(baixo == alto):
        break
    
    medio = int((baixo + alto )/ 2)
    print(medio)

    if( busca < vet[medio]):
        alto = medio + 1

    else:
        if( busca > vet[medio]):
            baixo = medio + 1

        else:
            achou = 1
		
if(achou == 1):
	print("FOI ENCONTRADO")

else:
	print("NÃO FOI ENCONTRADO")

# Base-de-Algoritmos-em-C_v2 / listavetoresmatrizesestrings7.c

numeros = []

pares = []

imapres = []

for i in range (5):
    num = int(input(f"Digite o valor do {i + 1} número: "))
    
    numeros.append(num)
    
    if num % 2 == 0:
        pares.append(num)
    else:
        imapres.append(num)
        
print("Números pares adicionados: ")
for i in range(0, len(pares)):
    print(pares[i])
    
print("Números ímpares adicionados: ")
for i in range(0, len(imapres)):
    print(imapres[i])
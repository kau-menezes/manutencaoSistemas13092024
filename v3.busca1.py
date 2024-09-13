# Base-de-algoritmos-em-C-v3 / busca1.c

valores = []
busca = 0
achou = 0

for i in range (10):
    res = input((f"Digite o valor {i + 1} da lista: "))
    valores.append(res)
    
busca = input(("Digite um valor a ser buscado na lista: "))
print(busca)

for i in valores:
    print(i)

for i in valores:
    print(i)
    if i == busca:
        achou+=1 

print(f"O valor {busca} foi encontrado {achou} vezes")
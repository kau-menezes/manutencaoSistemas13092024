# Base-de-Algoritmos-em-C_v2/listalaco_sexoaltura.c

print("\n\n #######################################")
print("\n\n           ANÁLISE DE FICHAS")
print("\n\n #######################################")

generos = []
alturas = []
soma_mulher = 0
qtd_muie = 0
qtd_home = 0
soma_home = 0
maior = 0

for i in range(4):
    genero = int(input("Digite seu gênero. 1 para Homem ou 2 para Mulher."))
    generos.append(genero)
    altura = float(input("Digite sua altura. "))
    alturas.append(altura)
    
    if genero == 2:
        soma_mulher = soma_mulher + altura
        qtd_muie += 1
        
    else:
        soma_home = soma_home + altura
        qtd_home += 1
        
        
for i in range(4):
    if alturas[i] > maior:
        maior = float(i)
        
print(f"Média de altura das mulheres: {soma_mulher / qtd_muie}")
print(f"Média de altura dos homens: {soma_home / qtd_home}")
print(f"Média das alturas {alturas / 4}")
print(f"Maior altura: {maior}")

    
    

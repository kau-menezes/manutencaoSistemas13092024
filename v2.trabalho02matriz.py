# # Base-de-Algoritmos-em-C_v2 /trabalho02matriz.c

matriz1 = []

for i in range(3):    
    a = []
    for j in range(3):   
        a.append(int(input(f"Digite o valor da linha {i} coluna {j} da matriz 1: ")))
    matriz1.append(a)

    
matriz2 = []

for i in range(3):    
    a = []
    for j in range(3):   
        a.append(int(input(f"Digite o valor da linha {i} coluna {j} da matriz 2: ")))
    matriz2.append(a)
    
matriz_resultado = []

for i in range(3):    
    a = []
    for j in range(3):   
        a.append((matriz1[i][j] + matriz2[i][j]))
    matriz_resultado.append(a)
    


for i in range(3):
    for j in range(3):
        print(matriz1[i][j], end=" ")
    print()
    
for i in range(3):
    for j in range(3):
        print(matriz2[i][j], end=" ")
    print()
    
for i in range(3):
    for j in range(3):
        print(matriz_resultado[i][j], end=" ")
    print()
    
diagonal = 0

for i in range (3):
    diagonal = diagonal + matriz_resultado[i][i]

print(f"O valor da Diagonal Principal é {diagonal}")
# Base-de-algoritmos-em-C-v3 /trabalho_moldularizacao.c

def calculo(n):
    return (float(n[0]) + float(n[1]) + float(n[2]) + float(n[3]) / 4)

n = []

name = input("Digite seu nome: ")

matricula = input("Digite sua matrícula: ")

for i in range(4):
    n.append(input(f"Digite a {i + 1}a nota: "))

res = calculo(n)

print(f"O(a) aluno(a) {name} de matrícula {matricula} obteve {res} de média.")
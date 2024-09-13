# Base-de-Algoritmos-em-C_v2 / revisao1.c

times = 0

while (True):
    time = input("Infomre o código do seu time: ")
    
    ages = 0
    
    for i in range(2):
        nome = input(f"Digite o nome do {i  + 1}° jogador: ")
        age = int(input(f"Digite a idade do(a) jogador(a) {nome}: "))
        ages = ages + age
    
    print(f"A média de idades do time é de {float(ages / 2)} anos")
    times += 1
    
    res = input("Deseja sair do programa? Digite 0.")
    
    if res == 0:
        print(f"Times calculados: {times}")
# Base-de-Algoritmos-em-C /sistematabuadas.c

res = 1

while(True):
    tabuada = input("Digite a tabuada que gostaria de verificar: ")
    
    for i in range (10):
        print(f"{i + 1} * {int(tabuada)} = {(i + 1) * int(tabuada)}")
    
    res = int(input("Deseja sair do programa? Digite 0 para sair."))
    
    if (res == 0):
        print("Tchau!")
        break
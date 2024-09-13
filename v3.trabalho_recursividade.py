# Base-de-algoritmos-em-C-v3 /trabalho_recursividade.c


def soma( x, y):
    
    if y == 1:
        return x
    else:
        return x + soma(x, y-1)
    

multiplicando = input("Informe o multiplicando: ")

multiplicador = input("Informe o multiplicador: ")

produto = soma(int(multiplicando), int(multiplicador))

print(f"A soma do multiplicando pelo número de vezes do multiplicador é: {produto}")
    

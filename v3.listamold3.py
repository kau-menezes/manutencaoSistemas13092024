n1 = float(input("Digite o valor do primeiro número: "))
n2 = float(input("Digite o valor do segundo número: "))
res = 0
de_novo = 1

while (True):
    
    op = int(input("Digite a operação que deseja realizar:\n1- Adição\n2- Subtração\n3-Multipplicação\n4-Divisão"))
    
    match (op):
        case 1:
            res = n1 + n2
            break
        
        case 2:
            res = n1 - n2
            break
    
        case 3:
            res = n1 * n2
            break
    
        case 4:
            if n2 == 0:
                print("NÃO É POSSÍVEL DIVIDIR POR 0")
                break
            
            res = n1 / n2
            break
        
    print(f"O resultado da operação é de: {res}")
    
    de_novo = int(input("Deseja sair do programa? Digite 0."))
    
    if (de_novo == 0):
        break
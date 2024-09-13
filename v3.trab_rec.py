# Base-de-algoritmos-em-C-v3 / trab_rec.c

def mns(senhordagloria, oq_esta_contecendo):
    
    if(oq_esta_contecendo == 1):
        
        return senhordagloria
    
    else:
        return senhordagloria + mns(senhordagloria, oq_esta_contecendo-1)
    
n1 = int(input("Digite um valor númerico: "))
nx_n1 = int(input("Digite o número de vezes que o número será somado: "))
resp = 0


    
resp = mns(n1, nx_n1)
    
print(f"RESPOSTA: {resp}")



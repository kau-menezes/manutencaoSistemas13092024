# Base-de-Algoritmos-em-C /inssIR.c

dependentes = int(input("Informe quantos dependetensvocê tem: "))

for i in range(12):
    renda_mensal = float(input(f"Informe sua renda mensal do {i + 1}° mês do ano: "))
    
    if renda_mensal >= 1399.12:
        valorinss = renda_mensal*0.08
        
    elif renda_mensal >= 1399.12 and renda_mensal <= 2331.88:
        valorinss = renda_mensal*0.09
    
    elif renda_mensal >= 2331.89 and renda_mensal < 4663.75:
        valorinss = renda_mensal*0.11
        
    else: 
        valorinss = 513.01
        
print(f"Valor INSS mensal: {valorinss}")
            

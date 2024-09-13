# Base-de-algoritmos-em-C-v3 /listamold1.c

import math

def calculo(litro, total):
    return float(total) / float(litro)

nome = input("Digite seu nome: ")

valor_litro = ""
pgto = ""

while not math.isnan(valor_litro):
    valor_litro = input(("Digite o preço do litro do combustível: "))
    
while not math.isnan(pgto):
    pgto = input(("Informe o valor da compra total: "))



print(f"A quantidade de combustível, em litros, que se pode comprar é de: {calculo(valor_litro, pgto)}")




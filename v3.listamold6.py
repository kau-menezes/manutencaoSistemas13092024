def calculo(p, m, g):
    return ((p * 10) + (m * 15) + (g * 20))


p = int(input("Informe a quantidade de camisas P a serem compradas (R$ 10,00): "))
m = int(input("Informe a quantidade de camisas M a serem compradas (R$ 15,00): "))
g = int(input("Informe a quantidade de camisas G a serem compradas (R$ 20,00): "))

print(f"Total a ser pago na compra: {calculo(p, m, g)}")
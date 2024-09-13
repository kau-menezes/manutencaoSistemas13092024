# Base-de-Algoritmos-em-C_v2 /trabalhostructIPTU.c

class imovel():
    
    def __init__(self, cadastro, valorIPTU, meses_atraso, multa):
        self.cadastro = cadastro
        self.valorIPTU = valorIPTU
        self.atraso = meses_atraso
        self.multa = multa
    
    def __str__(self):
        print(f"Imóvel de n° {self.cadastro}, com IPTU no valor de {self.valorIPTU} e multa no valor de {self.multa} após {self.atraso} meses de atraso.")
        
calculados = []

for i in range(3):
    cad = input(f"Informe o número do cadastro do imóvel {i + 1}: ")
    valor = float(input(f"Informe o valor do IPTU do imóvel {i + 1}: "))
    meses = int(input(f"Informe os meses de atraso do pagamento do imóvel {i + 1}: "))
    
    novo_imovel = imovel(cad, valor, meses, (meses * 50))
    calculados.append(novo_imovel)
    
for i in range(3):
    print(calculados[i].__str__())
        


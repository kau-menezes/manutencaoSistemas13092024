# Base-de-Algoritmos-em-C_v2 / aulapraticastruct.c

class pessoa():
    
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

    
    def __str__(self):
        print(f"Cidadão de nome {self.nome} de telefone {self.telefone}, morador(a) na rua: {self.endereco.__str__()}")
        
class endereco():
    def __init__(self, rua, numero, bairro, cep, cidade, estado):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.estado = estado
        
    def __str__(self):
        print(f"{self.rua}, {self.numero}, {self.bairro}, {self.cep}, {self.cidade}, {self.estado}")
        
        
nome = input("Digite seu nome: ")
telefone = input("Digite seu telefone: ")
rua = input("Digite sua rua: ")
numero = input("Digite o número de sua casa: ")
bairro = input("Digite seu bairro: ")
cep = input("Digite seu CEP: ")
cidade = input("Digite sua cidade: ")
estado = input("Digite a sigla do seu estado: ")

novo_endereco = endereco(rua, numero, bairro, cep, cidade, estado)

nova_pessoa = pessoa(nome, telefone, novo_endereco)        

print(nova_pessoa.__str__())


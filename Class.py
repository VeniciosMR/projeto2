# Programa da segunda atividade do curso Ponta Pé Dev
import re

def nova_pessoa():
    print('Adicionando uma nova pessoa!')
    nome = input('Digite o nome: ')
    while not re.match(r"^[A-Za-záàâãéèêíïóôõöúçÁÀÂÃÉÈÍÏÓÔÕÖÚ ]+$", nome):
        print('Nome invalido! Deve conter apenas letras e espaço.')
        nome = input('Digite o nome: ')
    nome = nome.capitalize()
    
    idade = input('Digite a idade: ')
    while not re.match(r"^[0-9]+$", idade) or -1 < int(idade) > 135:
        print('Idade invalida! Deve conter apenas numeros.')
        idade = input('Digite a idade: ')
    idade = int(idade)

    altura = input('Digite a altura em metros: ')
    altura = re.sub(r',', '.', altura)
    while not re.match(r"^[0-2]+[,.][0-9]+$", altura) or 0.1< float(altura) >2.8:
        print('altura invalida! Deve conter apenas numeros, com ponto ou virgula. Ex: 1,65')
        altura = input('Digite a altura em metros: ')
        altura = re.sub(r',', '.', altura)
    altura = float(altura)

    peso = input('Digite o peso: ')
    while not re.match(r"^[0-9]+$", peso) or 0 < int(peso) > 600:
        print('Valor invalido! Deve conter apenas numeros.')
        peso = input('Digite o peso: ')
    peso = int(peso)

    nascimento = input('Digite a data de nascimento (DD/MM/AAAA): ')
    while not re.match(r"^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$", nascimento):
        print('Data invalida! Deve conter numeros e barra. Ex 01/01/2001')
        nascimento = input('Digite a data de nascimento: ')
    
    print('Nova pessoa adicionada!')
    
    return(Pessoa(nome, idade, altura, peso, nascimento))

class Pessoa:
    def __init__(self, nome:str, idade:int, altura:float, peso:float, nascimento:str):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.nascimento = nascimento
    
    def eh_maior(self):
        if self.idade > 17:
            maior = True
        else:
            maior = False
        return maior
    
    def imc(self):
        return self.peso / (self.altura * self.altura)
    
    def imc_longo(self):
        if self.imc() < 18.5:
            return "abaixo do peso"
        elif 18.5 <= self.imc() < 25:
            return "peso normal"
        elif 25 <= self.imc() < 30:
            return "sobrepeso"
        elif 30 <= self.imc() < 35:
            return "obesidade grau I"
        elif 35 <= self.imc() < 40:
            return "obesidade grau II"
        else:
            return "obesidade grau III"
        
    def apresentar(self):
        print(f'Aoba!!! Me chamo {self.nome} e tenho {self.idade} anos.')
    
    def compara_idade(self, idade:int):
        if idade > self.idade:
            print(f'Essa outra pessoa e mais velha do que {self.nome}')
        elif idade == self.idade:
            print('Os dois tem a mesma idade.')
        elif idade < self.idade:
            print(f'Essa outra pessoa e mais nova do que {self.nome}')
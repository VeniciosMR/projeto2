# Programa da segunda atividade do curso Ponta Pé Dev

class Pessoa:
    def __init__(self, nome:str, idade:int, altura:float, peso:float):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
    
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
            return "Abaixo do peso"
        elif 18.5 <= self.imc() < 25:
            return "Peso normal"
        elif 25 <= self.imc() < 30:
            return "Sobrepeso"
        elif 30 <= self.imc() < 35:
            return "Obesidade grau I"
        elif 35 <= self.imc() < 40:
            return "Obesidade grau II"
        else:
            return "Obesidade grau III"
        
    def apresentar(self):
        print(f'Aoba!!! Me chamo {self.nome} e tenho {self.idade} anos.')
    
    def compara_idade(self, idade:int):
        if idade > self.idade:
            print(f'Essa outra pessoa e mais velha do que {self.nome}')
        elif idade == self.idade:
            print('Os dois tem a mesma idade.')
        elif idade < self.idade:
            print(f'Essa outra pessoa e mais nova do que {self.nome}')

pessoas = []
p = Pessoa('Venicios', 25, 1.88, 70)
pessoas.append(p)
p = Pessoa('Thomaz', 24, 1.75, 80)
pessoas.append(p)

# pessoas[0].compara_idade(pessoas[1].idade)
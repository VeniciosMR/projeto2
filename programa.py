from Class import Pessoa
import random

pessoas = []
p = Pessoa('Venicios', 25, 1.88, 70)
pessoas.append(p)
p = Pessoa('Thomaz', 2077, 1.75, 82)
pessoas.append(p)
p = Pessoa('Heloisa', 23, 1.6, 68)
pessoas.append(p)
p = Pessoa('Henzo', 13, 1.47, 59)
pessoas.append(p)
p = Pessoa('Junior', 15, 1.9, 80)
pessoas.append(p)

# Mostra todos da lista
print('Pessoas da lista:')
for pessoa in pessoas:
    print(pessoa.nome.capitalize())
# Mostra apenas quem e de maior
print('\nPessoas maiores de idade na lista:')
for pessoa in pessoas:
    if pessoa.idade > 17:
        print(pessoa.nome.capitalize())


# Dados de alguem da lista
# Apresentação de uma pessoa aleatoria
p = random.choice(pessoas)
print('\nDados de alguem da lista:')
print(f'Olá, meu nome é {p.nome}, tenho {p.idade} anos.')

# Mostar IMC da pessoa aleatoria e sua faixa de peso
print(f'O IMC do(a) {p.nome} é {p.imc():.2f}.')
print(f'A faixa de peso do(a) {p.nome} é {p.imc_longo()}.')

# pessoas[0].compara_idade(pessoas[1].idade)
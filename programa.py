from Class import *

# Adicionando pessoas
pessoas = []
pessoas.append(nova_pessoa())
p = Pessoa('Thomaz', 2077, 1.75, 82, '01/01/-0053')
pessoas.append(p)
p = Pessoa('Heloisa', 23, 1.6, 68, '30/08/2000')
pessoas.append(p)
p = Pessoa('Henzo', 13, 1.47, 59, '01/01/2001')
pessoas.append(p)
p = Pessoa('Junior', 15, 1.9, 80, '01/01/2001')
pessoas.append(p)

# Mostra todos da lista
print('\nPessoas da lista:')
for pessoa in pessoas:
    print(pessoa.nome)
# Mostra apenas quem e de maior
print('\nPessoas maiores de idade na lista:')
for pessoa in pessoas:
    if pessoa.idade > 17:
        print(pessoa.nome)


# Dados da pessoa nova
p = pessoas[0]
print(f'\nDados de {p.nome}:')
print(f'Olá, meu nome é {p.nome}, tenho {p.idade} anos.')

# Mostar IMC da pessoa aleatoria e sua faixa de peso
print(f'O IMC do(a) {p.nome} é {p.imc():.2f}.')
print(f'A faixa de peso do(a) {p.nome} é {p.imc_longo()}.')

# pessoas[0].compara_idade(pessoas[1].idade)
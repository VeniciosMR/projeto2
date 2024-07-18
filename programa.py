from Class import Pessoa

pessoas = []
p = Pessoa('Venicios', 25, 1.88, 70)
pessoas.append(p)
p = Pessoa('Thomaz', 2077, 1.75, 80)
pessoas.append(p)
p = Pessoa('Heloisa', 23, 1.60, 72)
pessoas.append(p)

pessoas[0].compara_idade(pessoas[1].idade)
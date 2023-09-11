# Solicita a quantidade de ativos ao usuário
quantidade_ativos = int(input())

# Inicializa uma lista vazia para armazenar os ativos
ativos = []

# Solicita os tipos de ativos ao usuário e os adiciona à lista
for _ in range(quantidade_ativos):
    ativo = input()
    ativos.append(ativo)

# Ordena a lista de ativos em ordem alfabética
ativos.sort()

# Exibe os ativos em ordem alfabética
for ativo in ativos:
    print(ativo)
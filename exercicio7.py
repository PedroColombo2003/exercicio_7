"""
Titulo: Exercicio 6
Autor: Pedro Colombo
Data: 25/02/2025
Versão: 0.0.1

Problema: determine o n-esimo termo e a soma dos termos de uma progressao geometrica onde n, primeiro termo e a razao sao dados pelo usuario.

"""

# Entrada de dados

primeiro_termo = int(input("Escolha um primeiro termo: "))

razao = int(input("Qual será a razão entre os termos? "))

n = int(input("Escolha um N (posição do termo) "))

# Processamento de dados
termo_n = primeiro_termo * (razao ** (n - 1))


# Saida de dados

print(f"o valor do termo que está na posição {n} é {termo_n}")

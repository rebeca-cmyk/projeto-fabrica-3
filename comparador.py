produto = input("produto: ")
nome_mercado = input("nome do mercado: ")
preco_produto1 = float(input("preco do produto: "))
nome_mercado2 = input("nome do mercado2: ")
preco_produto2 = float(input("preco do produto: "))
nome_mercado3 = input("nome do mercado: ")
preco_produto3 = float(input("preco do produto: "))

if preco_produto1 < preco_produto2 and preco_produto1<preco_produto3:
    print(f"{produto}, {nome_mercado1}, {preco_produto1}")
elif preco_produto2<preco_produto1 and preco_produto2<preco_produto3:
    print(f"{produto}, {nome_mercado2}, {preco_produto2}")
else:
    print(f"{produto}, {nome_mercado3}, {preco_produto3}")
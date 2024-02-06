
# acima de 15000 -> 500 de bonus 
# acima de 10000 -> 150 de bonus
# acima de 5000 -> 50 de bonus
# vendas da empresa -> 50000

vendas = 17000
vendas_empresa = 60000
meta_empresa = 50000

if vendas > 15000 and vendas_empresa >= meta_empresa:
    bonus = 500
elif vendas > 10000 and vendas_empresa >= meta_empresa:
    bonus = 150
elif vendas > 5000 and vendas_empresa >= meta_empresa:
    bonus = 50
else:
    bonus = 0

print("Bonus", bonus)

# utra maneira de fazer
# if vendas > 5000:
#     if vendas > 10000:
#         if vendas > 15000:
#             bonus = 500
#         else:
#             bonus = 150
#     else:
#         bonus = 50
# else:
#     bonus = 0
# 
# print("Bonus", bonus)


if not vendas_empresa > meta_empresa:
    bonus = 0
else:
    if vendas > 15000:
        bonus = 500
    elif vendas > 10000:
        bonus = 150
    elif vendas > 5000 :
        bonus = 50

print("Bonus", bonus)

#exercicio desafio
#sistema de consulta de preço
precos = [1500, 100, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]
produto_procurado = input("Digite um produto: ")
produto_procurado = produto_procurado.lower() # o lower() converte tudo para minusculo 

if produto_procurado in produtos:
    print("Produto encontrado")
    posicao = produtos.index(produto_procurado)
    print(f"Produto: {produto_procurado}, Preço: {precos[posicao]}")
else:
    print("Produto não encontrado")





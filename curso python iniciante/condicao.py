faturamento = 1000
custo = 800

lucro = faturamento - custo

if lucro >= 0:  #no python a identação é obrigatória 
    print(lucro)
else:
    print("Prejuizo!!!!")
    print(lucro)

produto = ["iphone", "ipad", "airpod"]
novo_produto = input("Digite novo produto:")
novo_produto = novo_produto.lower() #para deixar tudo em minusculo

if novo_produto in produto:
    print("Produto já cadastrado")
else:
    print("Produto cadastrado")
    produto.append(novo_produto)

print(produto)
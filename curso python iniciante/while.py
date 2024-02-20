produtos = ["celular", "camera", "fone de ouvido", "monitor"]

while True:
    
    novo_produto = input("Digite um produto: ")
    novo_produto = novo_produto.lower() # o lower() converte tudo para minusculo 

    if "sair" == novo_produto:
        break

    if novo_produto in produtos:
        print("Produto ja cadastrado")    
    else:
        print(f"Produto {novo_produto} cadastrado com sucesso")
        produtos.append(novo_produto)

print(produtos)
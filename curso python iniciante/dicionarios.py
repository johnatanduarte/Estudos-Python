precos = [1500, 100, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

dic_precos = {"celular": 1500, "Camera": 1000, "fone de ouvido": 800, "monitor": 2000}

#pegar um item
preco_celular = dic_precos["celular"]
print(preco_celular)

dic_precos["celular "] = 2000 #editando o preco do celular
print(dic_precos)

dic_precos["iphone"] = 4500 #quando se edita um item que não existe no dicionario, voce adiciona ele na lista
print(dic_precos)

dic_precos.pop("iphone")
print(dic_precos)

#tamanho dicionario
print(len(dic_precos))
print("celular" in dic_precos)   #pra ver se tem a chave celular 
print(1500 in dic_precos.values()) #pra ver se tem o valor 1500

#exercicio
dic_precos = {"celular": 1500,
               "camera": 1000, 
               "fone de ouvido": 800, 
               "monitor": 2000
            }

produto_procurado = input("Digite um produto para ver o preco: ")
produto_procurado = produto_procurado.lower()  # o lower() converte tudo para minusculo 

if produto_procurado in dic_precos:
    print("Produto encontrado")
    preco = dic_precos[produto_procurado]
    print(f"Produto: {produto_procurado}, preço: {preco}")
else:
    print("Produto não encontrado, tente novamente")


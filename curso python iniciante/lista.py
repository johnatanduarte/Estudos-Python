vendas = [100, 50, 130, 80, 120]
print(vendas[0]) #primeito elemento
print(vendas[-1]) #ultimo elemento

total_vendas = sum(vendas)
print(total_vendas)
quantidade = len(vendas)
print(quantidade)
valor_max = max(vendas)
valor_min = min(vendas)
print(valor_max, valor_min)

posicao = vendas.index(130) # index é uma função para encontrar a posição na lista
print(posicao)

produto = ["iphone", "ipad", "airpod"]
print("iphone" in produto) #in -> o produto contem iphone? True or Not
produtos_usuario = input("Digite o nome de um produto: ")
print(produtos_usuario in produto)

#editar o valor na lista
precos = [4000, 8000, 2000]
precos[0] = 4500
print(precos)

precos[0] = precos[0] * 1.1  #aumentando o valor em 10%
print(precos)

#adicionar um item na lsita
produto.append("macbook")
precos.append(10000)
print(produto)
print(precos)

#remover um item
produto.remove("macbook") #remove pelo valor
precos.pop(-1) #remove pelo indice
print(produto, precos)  

#inserir em determinada posição 
produto.insert(1, "airpod")
print(produto)

#contar valores
print(produto.count("airpod"))

#ordenar
precos.sort(reverse=True) #ordem inversa
print(precos)
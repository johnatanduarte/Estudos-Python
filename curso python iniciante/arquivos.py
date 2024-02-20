
#arquivo = open("vendas.txt", "r") #posso passar o vendas.txt direto pq esta no mesmo local do arquivo

 #fazer algo com o arquivo
#arquivo.close()


#Usando o with não precisa fechar o arquivo
with open("curso python iniciante/vendas.txt", "r") as arquivo: 
    infos = arquivo.readlines()

vendas_totais = 0
for item in infos:
    item = item.replace("\n", "")
    item = item.replace(" ", "")
    resultado = item.split(",") #split separa!
    valor = resultado[1]
    valor = float(valor)
    vendas_totais = vendas_totais + valor

print(vendas_totais)



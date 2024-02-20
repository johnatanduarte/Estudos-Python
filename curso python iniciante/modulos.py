#biliotecas
#os e a requests

import os 

list_arquivos = os.listdir("curso python iniciante/arquivos") #listdir -> lista o diretorio 
print(list_arquivos)

for nome_arquivo in list_arquivos:
    if "txt" in nome_arquivo:
        if "22" in nome_arquivo:
            os.rename(f"curso python iniciante/arquivos/{nome_arquivo}", f"curso python iniciante/arquivos/22/{nome_arquivo}")
        elif "23" in nome_arquivo:
            os.rename(f"curso python iniciante/arquivos/{nome_arquivo}", f"curso python iniciante/arquivos/23/{nome_arquivo}")

# movimentar arquivos
# os.rename("curso python iniciante/vendas.txt", "curso python iniciante/arquivos/vendas.txt")
            
import requests

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

resposta = requests.get(link)
dic_resposta = resposta.json()
#print(dic_resposta)
cotacao_dolar = dic_resposta["USDBRL"]
print(cotacao_dolar["bid"])

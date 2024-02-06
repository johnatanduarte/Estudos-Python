faturamento = 1000
custo = 700
lucro = faturamento - custo
margem = lucro/faturamento

#concatenando textos 
print(f"faturamento: {faturamento:,.2f}, Custo: {custo}, Lucro: {lucro}")
print(f"faturamento: "  + str(faturamento) + ", custo: " + str(custo) + ", lucro: " + str(lucro))
print(f"margem: {margem:.1%}")

email = "eMAil_falso@gmail.com"
print(email.lower()) #lower serve para colocar tudo em letra minuscula 
print(email.find("@")) #função para encontrar a posiçaõ do elemento. E -1 se ñ encontrar o elemento 

posicao = email.find("@")
servidor = email[posicao+1:]
print(servidor)
outra_forma = email[:posicao]
print(outra_forma)

#tamanho do texto
tamanho = len(email)
print(tamanho)

#trocar um pedaço do texto
email_trocado = email.replace("gmail", "hotmail")
print(email_trocado)

nome = "johnatan duarte"
print(nome.capitalize()) #capitalize coloca a Primera letra em maiuscula no inicio da frase
print(nome.title()) #title coloca a primeira letra maiuscula em cada palavra





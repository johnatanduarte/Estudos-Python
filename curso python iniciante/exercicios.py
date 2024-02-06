#exercicio
nome = "Johnatan Duarte Franco"
email = "johnatanduartefranco95@gmail.com"

#descubra o servidor do email
posicao_serv = email.find("@")
print(email[posicao_serv:])

#pegar o 1° nome do usuario
first_name = nome.find(" ")
print(nome[:first_name]) #o dois ponrtos : pode significar até

#construa uma mensagem: Usuario primeiro_nome cadastrado com sucesso com o email
print("Usuario", nome[:first_name], "cadastrado com sucesso com o email:", email)

#construa uma mensagem: Enviamos um link de confirmação para o email j***@gmail.com
print("Enviamos um link de confirmação para o email", nome[0],"***",email[posicao_serv:])
print(f"Enviamos um link de confirmação para o email {nome[0]}***{email[posicao_serv:]}")
faturamento = 1000
cursto = 700
novas_vendas = 300
faturamento = faturamento + novas_vendas
lucro = faturamento - cursto
imposto = faturamento * 0.1
print(faturamento)
print(lucro)
margem_lucro = lucro / faturamento
print(margem_lucro)
restituicao = imposto * 0.1
print(restituicao)
#restituicao = faturamento ** 0.1     serve para elevar, ex: faturamento^0.1 
print(restituicao)

# mod resto da divisão
# 10 % 3
tempo_em_meses = 160
#tempo_em_anos = tempo_em_meses / 12
tempo_em_anos = int(tempo_em_meses / 12)
print(tempo_em_anos)
print(tempo_em_meses % 12)

#round -> arredondadmento da forma matematica
numero = 123.60
print(round(numero))

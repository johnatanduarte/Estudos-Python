#2:47

for i in range(10):
    print("fala tu")

lista_precos = [1500, 1000, 800, 2000]
imposto = 0.1

#precos[0]*0.1
#precos[1]*0.1
#precos[2]*0.1

for preco in lista_precos:
    imposto = preco*0.1
    print(f"preco {preco}, Imposto: {imposto}")

# regra de imposto 
# se o preco é ate 1000 o imposto é de 10%
# se o preco é maior do que 1000 o imposto é de 15%
print("-------------------------")

total_imposto = 0
for preco in lista_precos:
    if preco <= 1000:
        imposto = preco*0.1
        
    elif preco > 1000:
        imposto = preco*0.15
    print(f"preço: {preco}, imposto: {imposto}")
    total_imposto += imposto

print(f"Total de imposto: {total_imposto}")

#Esxercicio
#Saber quanto variou percentualmente cada mes de 2023 em comparação com 2022

vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}

for mes in vendas_23:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    variac_percentual = valor_23 / valor_22 - 1
    print(f"Variação do {mes}: {variac_percentual:.1%}")

print(f"Faturamento total do ano de 2022: {sum(vendas_22.values())}")
print(f"Faturamento total do ano de 2023: {sum(vendas_23.values())}")
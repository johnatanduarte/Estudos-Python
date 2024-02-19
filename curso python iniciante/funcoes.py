#3:15:15
lista_precos = [1500, 1000, 800, 2000]

total_imposto = 0 #acumulado

def calcular_imposto(preco, aliquota1, aliquota2):
    if preco > 1000:
        imposto = preco * aliquota1
    else:
        imposto = preco * aliquota2
    print(f"Preço: {preco}, Imposto: {imposto}")
    return imposto

for preco in lista_precos: #1000
    imposto = calcular_imposto(preco, 0.15, 0.1)
    
    total_imposto += imposto

print(total_imposto)

def calcular_imposto2(preco, ir=0.275, csll=0.035, iss=0.05):
    imposto_ir = preco * ir
    imposto_csll = preco * preco * csll
    imposto_iss = preco * iss
    return imposto_ir, imposto_csll, imposto_iss

resposta = calcular_imposto2(1000)
print(resposta)



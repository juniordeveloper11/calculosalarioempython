salario_bruto = float(input("digite o salario bruto :"))

taxa_imposto_10 = 0.1
taxa_imposto_20 = 0.2
taxa_imposto_30 = 0.3

if salario_bruto <= 2000:
    imposto = salario_bruto * taxa_imposto_10
elif salario_bruto <= 5000:
    imposto = salario_bruto * taxa_imposto_20
else:
    imposto =salario_bruto *taxa_imposto_30        

salario_liquido = salario_bruto  - imposto

print("imposto de renda:" ,imposto)
print("salario liquido:" , salario_liquido)
def calcular_percentual(valor,total):
    return(valor/total)*100

salario = float(input("Digite o valor do salario mensal: R$ "))

#gasto por enquato estar manual 
gastos = {}

while True:
    categoria = input("Digite o nome da categoria de gasto(ou 'sair' para finalizar): ")
    if categoria.lower() == 'sair':
        break
    valor = float(input(f"Digite o valor em {categoria}: R$ "))
    gastos[categoria] = valor

    # analise do valores
    print ("n----RELATORIO FINANCEIRO---")
    total_gastos = sum(gastos.values())
    saldo = salario - total_gastos

    for categoria, valor in gastos.items():
        percentual = calcular_percentual(valor, salario)
        print(f"{categoria}: R$ {valor:.2f} ({percentual:.1f}%)")

        
print(f"\nTotal gasto: R$ {total_gastos:.2f}")
print(f"Saldo restante: R$ {saldo:.2f}")

if saldo < 0:
    print("⚠️ Atenção: você gastou mais do que ganha!")
else:
    print("✅ Parabéns! Você está dentro do seu orçamento.")
salario = float(input("Digite o valor do seu salário mensal R$: "))
produto = float(input("Digite o valor do produto R$: "))
horas_mes = float(input("Quantas horas Você trabalha no mês ? (ex:160): "))

porcentagem = (produto/salario) * 100
valor_hora = salario/horas_mes
horas_necessarias = produto/valor_hora
dias_necessarios = horas_necessarias/8

print("\n📊 RESULTADO:")
print(f"O produto representa {porcentagem:.2f}% do seu salário.")
print(f"Você ganha aproximadamente R$ {valor_hora:.2f} por hora.")
print(f"Você precisa trabalhar cerca de {horas_necessarias:.1f} horas para comprar o produto.")
print(f"Isso equivale a aproximadamente {dias_necessarios:.1f} dias de trabalho.")

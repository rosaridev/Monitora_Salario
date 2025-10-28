salario = float(input("Digite o valor do seu salario: "))

investimento = salario *0.2
seguro = salario*0.1
contas_fixas = salario*0.6
lazer = salario*0.1

print("---> valores com a divisão sugeridas: ")
print(f"para investimento 20% {investimento:.2f}")
print(f"para seguro 10% {seguro:.2f}")
print(f"para contas fixas 60% {contas_fixas:.2f}")
print(f"para lazer 10% {lazer:.2f}")
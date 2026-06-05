salario = float(input("digite seu salario mensal: "))
lazer = float(input("quanto voce gasta com lazer? : "))
fixas = float(input("quanto e suas contas fixas? :  "))
investimento = float(input("quanto e suas contas investimento? :  "))
seguro = float(input("quanto e suas contas seguro? :  "))

porc_investimento= (investimento/salario)*100
porc_seguro = (seguro/salario)*100
porc_lazer = (lazer/salario)*100
porc_fixas = (fixas/salario)*100

print(f"seu gasto em % do salario com lazer é: {porc_lazer}%")
print(f"seu gasto em % do salario com fixas é: {porc_fixas}%")
print(f"seu gasto em % do salario com investimento é: {porc_investimento}%")
print(f"seu gasto em % do salario com seguro é: {porc_seguro}%")
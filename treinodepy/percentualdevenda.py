fat = 50000
perc_bonus = 0.10
fun = 0



fun = int(input("Digite o numero de funcionarios: "))

bonus_total = fat * perc_bonus
bonus_por_vendedor = bonus_total / fun
fat_liquido = fat - bonus_total


print(f"O faturamento Bruto: R$ {fat:.2f} e o faturamento liquido é: R$ {fat_liquido:.2f}")
print(f"O bonus total a ser pago é: R$ {bonus_total:.2f}")
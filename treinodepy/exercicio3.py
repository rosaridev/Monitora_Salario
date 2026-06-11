def calcular_salario(salario,seguro):
    if salario <= 0:
        return 0.0
    return salario - seguro

def calcular_seguro(salario):
    seguro = salario * 6
    return seguro
def divisao_por_mes(seguro):
    return seguro / 12

def main():
    salario = float(input("digite o valor do seu salario mensal: R$ " ))
    seguro = calcular_seguro(salario)
    valor_reserva = divisao_por_mes(seguro)
    print(f"valor da reserva de emergencia a se guardo pot mes durante um ano : R$ {valor_reserva:.2f}")
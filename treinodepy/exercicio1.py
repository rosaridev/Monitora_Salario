def calcular_percentual(gasto,salario):

    return (gasto/salario)*100

def classificar_gasto(percentual):
    if percentual > 40:
        return "gasto alto"
    elif percentual > 10:
        return "gasto moderado"
    else:
        return "gasto leve"
    
def pedir_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("Digite um valor positivo.")
                continue
            return valor
        except ValueError:
            print("valor Inválido. digite um numero.")
        

def main():
    salario = pedir_valor("Digite o valor do seu salário mensal: R$ ")
    gasto = pedir_valor("Digite o valor de gasto mensal: R$ ")

    percentual = calcular_percentual(gasto, salario)
    classificacao_gasto = classificar_gasto(percentual)

    print(f"\nR$ {gasto:.2f} representa {percentual:.1f}% do seu Salário.")
    print(f"Classificação do gasto: {classificacao_gasto}")


if __name__ == "__main__":
    main()
def pedi_valor(mensagem,tentativas=3):
    for i in range(tentativas):
        try:
            valor =float(input(mensagem))
            if valor <= 0:
                print(f"Valor invalido. {tentativas - i -1} tentativa(s) restante(s).")
                continue
            return valor
        except ValueError:
            print(f"Valor invalido. {tentativas - i -1} tentativa(s) restante(s).")
    return None

def calcular_percentual(gasto,salario):
    if salario ==0:
        return 0.0
    return (gasto / salario) * 100

def classificar_gasto(percentual):
    if percentual > 40:
        return "gastos altos"
    elif percentual > 10:
        return "gastos moderados"
    else:
        return "gastos leves"
    
def main():
    salario = pedi_valor("Digite o salario: R$ ")
    if salario is None:
        print("Valor do salário não fornecido. Encerrando o programa.")
        return
    gasto = pedi_valor("Digite o valor do gasto mensal: R$ ")
    if gasto is None:
        print("Valor do gasto não fornecido. Encerrando o programa.")
        return
    percentual = calcular_percentual(gasto,salario)
    classificacao = classificar_gasto(percentual)
    print(f"\nR$ {gasto:.2f} representa {percentual:.1f}% do seu salário.")
    print(f"Classificação do gasto: {classificacao}")

    if gasto > salario:
        print("Atenção! O gasto mensal é maior que o salário.")

    print(f"Classificação : {classificacao}")

if __name__ == "__main__":
    main()
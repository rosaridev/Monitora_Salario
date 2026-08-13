def calcular_salario(salario,seguro):
    if salario <= 0:
        return 0.0
    return salario - seguro

def calcular_seguro(salario):
    seguro = salario * 6
    return seguro
def divisao_por_mes(seguro,meses):
    return seguro /meses

def main():
    salario = float(input("digite o valor do seu salario mensal: R$ " ))
    meses = int(input("em quantos meses deseja dividir o seguro? "))
    seguro = calcular_seguro(salario)
    valor_reserva = divisao_por_mes(seguro,meses)
    print(f"-------É recomendado que você reserve 6 meses do seu salario que é: R$ {salario:.2f} para o seguro.--------")
    print(f"valor da Reserva: R$ {seguro:.2f}")
    print(f"valor da Reserva dividido {meses} o valor: R$ {valor_reserva:.2f}")

if __name__ == "__main__":
        main()
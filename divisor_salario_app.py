import PySimpleGUI as sg
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"  
os.environ["TK_SILENCE_DEPRECATION"] = "1"


sg.theme("DarkBlue3")

#layout da janela
layout = [
    [sg.Text("Digite o valor do seu salário:")],
    [sg.Input(key="Salario")],
    [sg.Button("Calcular"), sg.Button("sair")],
    [sg.Text("",key="Resultado", size =(40,5))]
]

#criação da janela
sg.set_options(icon=None)

janela = sg.Window("Divisor de salário", layout)

while True:
    evento, valores = janela.read()

    if evento == sg.WINDOW_CLOSED or evento == "sair":
    
        break

    if evento == "Calcular":
        try: 
            salario = float(valores("salario"))

            investimento = salario * 0.2
            seguro = salario * 0.1
            contas_fixa = salario * 0.6
            lazer = salario * 0.1

            resultado = (
                f"Investimento: R${investimento:.2f}\n"
                f"Seguro: R${seguro:.2f}\n "
                f"Contas essenciais: R${contas_fixa:.2f}\n"
                f"Lazer: R${lazer:.2f}"
            )

            janela["resultado"].update(resultado)
        except ValueError:
            janela["resultado"].update("Por favor, digite um valor numero válido!")
janela.close()


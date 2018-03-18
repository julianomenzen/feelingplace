import os

def atualizarProgresso(tabela, valoratual, total):
    percentual = (100 * valoratual) / total
    os.system('cls||clear')
    print("Importando tabela " + tabela + "\n")
    print(str(percentual) + "%")


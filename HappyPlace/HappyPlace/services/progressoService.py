import os
import sys
from time import sleep

def atualizarProgresso(tabela, valoratual, total):
    percentual = (100 * valoratual) / total
    print("Importando tabela " + tabela)
    saida = str( "%.2f" % percentual)
    print(saida)



import os
import sys
from time import sleep

def atualizarProgresso(tabela, valoratual, total):
    percentual = (100 * valoratual) / total
    print("\033[1;1fImportando tabela " + tabela + "\n")
    saida = str( "%.2f" % percentual)
    print("\033[2;1f" + saida)



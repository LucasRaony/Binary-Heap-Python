import math
from numpy import *
import heapBinario
import tratamentoDeArquivos

def main():
    #heap = [27,17,3,16,13,10,15,7,12,4,8,9,0]
    arquivo = 'couting.txt'
    heap = tratamentoDeArquivos.ler(arquivo)
    print('Array inicial\n',heap)
    resultado = heapBinario.heapSort(heap)
main()

import math
from numpy import *

def MaxHeapFY(heap, pos):
    left = 2*pos+1
    right = 2*pos+2
    tamanho = len(heap) - 1
    if left <= tamanho and heap[left] > heap[pos] :
        maior = left
    else:
        maior = pos
    if right <= tamanho and heap[right] > heap[maior] :
        maior = right
    if maior != pos:
        aux = heap[pos]
        heap[pos] = heap[maior]
        heap[maior] = aux
        MaxHeapFY(heap, maior)

def buildMaxHeap(heap):
    for i in reversed( range( len(heap)//2 ) ):
        #print(i)#i recebe posição da primeira sub árvore de nível profundidade-1
        MaxHeapFY(heap, i)
    print('\nHeap criado\n',heap)
      
def heapSort(heap):
    """
    1 - Construir a Heap
    2 - Trocar a raiz pelo último elemento
    3 - Remove esse valor do array
    4 - Chama MaxHeapFY pro primeiro elemento
    5 - Volta pro passo 2
    """
    resultado = [] #Cria uma lista vazia
    buildMaxHeap(heap)
    tamanho = len(heap)
    i = tamanho - 1
    while i>0:   #  0<i<tamanho-1
        aux = heap[0]
        heap[0] = heap[i]
        heap[i] = aux
        resultado.insert(0,heap.pop())#Insere o elemento removido na posição 0 da lista
        MaxHeapFY(heap, 0)
        i = i - 1
    resultado.insert(0,heap[0])
    heap.pop() #O heap antigo agora está vazio pra não disperdiçar memória
    print('\nHeap Ordenado\n',resultado)
    return resultado

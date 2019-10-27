def ler(nome):
    lista = []
    arquivo = open(nome, 'r')
    for palavra in arquivo:
        aux = palavra.split()
        lista.append(int(aux[0]))
    arquivo.close()
    return lista

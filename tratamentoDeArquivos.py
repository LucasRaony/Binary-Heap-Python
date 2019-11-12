def ler(nome):
    #TIPO 1:  Algoritmo para ler arquivos no formato
    """
    numero
    numero
    .
    .
    .
    numero
    """
    # TIPO 2:  Algoritmo para ler arquivos no formato (Esse é o melhor na minha opinião, pq vc pode manipular pra ler qualquer coisa
    """
    numero-numero-numero-......-numero
    .
    .
    .
    numero-numero-numero-......-numero
    """

    # TIPO 1:(Qualquer um deles funciona)
    """
    lista = []
    arquivo = open(nome, 'r')
    for palavra in arquivo:
        aux = palavra.split()
        lista.append(int(aux[0]))
    arquivo.close()
    return lista
    """
    """
    lista = []
    arquivo = open(nome, 'r')
    arquivo = arquivo.read()
    aux = 0
    numero = ''
    for i in arquivo:
        if arquivo[aux] != '\n':
            numero = numero + arquivo[aux]
        if arquivo[aux] == '\n':
            lista.append(int(numero))
            numero = ''
        aux = aux + 1
    return lista
    """
    # TIPO 2:
    
    lista = []
    arquivo = open(nome, 'r')
    arquivo = arquivo.read()
    aux = 0
    numero = ''
    
    for i in arquivo:
        if arquivo[aux] != ' ' and arquivo[aux] != '-' and arquivo[aux] != '\n':
            numero = numero + arquivo[aux]
        if arquivo[aux] == '-':
            lista.append(int(numero))
            numero = ''
        aux = aux + 1
    return lista
    
  

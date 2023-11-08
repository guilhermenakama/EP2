
import random

def filtra(palavras,num_letras):
    lista = []
    caract_especiais = ["?","!","@",".",",","~","^","´","`","-","_"]

    for palavra in palavras:

        if len(palavra) == num_letras:
            palavra = palavra.lower()

            for caracter in caract_especiais:
                texto_sem_especiais = palavra.replace(caracter,"")
            
            if palavra not in lista:
                lista.append(palavra)

    return lista


def inicializa(lista_palavras):

    dic = {}
    
    sorteada = random.choice(lista_palavras)
    n = len(sorteada)

    dic['sorteada'] = sorteada
    dic['n'] = n
    dic['especuladas'] = []
    dic['tentativas'] = n + 1

    return dic


def inidica_posicao(sorteada,especulada):

    resposta = []

    if len(sorteada) != len(especulada):
        return([])
    
    for i in range(len(sorteada)):
        
        if especulada[i] not in sorteada:
            resposta.append(2)
        elif especulada[i] == sorteada[i]:
            resposta.append(0)
        else:
            resposta.append(1)

    return resposta

from funcoes import *
from listas_palavras import base_palavras
import introducao

#Printar a tabela inicial
print(introducao)

num_letras = int(input("\n    Quantas letras na palavra? "))
tentativas = num_letras + 1

#Iniciando novo jogo
print("\n    Sorteando uma palavra...")

#Cria lista de palavras com 5 letras
lista_palavras = filtra(base_palavras,num_letras)

#Cria dicionario
dicionario = inicializa(lista_palavras)

#Escolhe palavra sorteada aleatoriamente
sorteada = dicionario['sorteada']

print("    Já tenho uma palavra! Tente adivinhá-la!")
print("\n    Você tem {0} tentaviva(s)".format(tentativas))

#Roda o jogo em looping
while True:

    especulada = input("    Qual seu palpite? ")

    #Roda o comando "desisto"
    if especulada.lower() == "desisto":

        jogo_novo = input("Jogar novamente? [s|n] ")

        #Sair do jogo
        if jogo_novo.lower() == "n":
            break
        #Iniciar novo jogo
        elif jogo_novo.lower() == "s":
            num_letras = int(input("\n    Quantas letras na palavra? "))
            tentativas = num_letras + 1
            print("\n    Sorteando uma palavra...")
            lista_palavras = filtra(base_palavras,num_letras)     #Cria lista de palavras com 5 letras
            dicionario = inicializa(lista_palavras)               #Cria dicionario
            sorteada = dicionario['sorteada']                     #Escolhe palavra sorteada aleatoriamente
            print("    Já tenho uma palavra! Tente adivinhá-la!")
    
    #Quando a palavra não possui 5 letras
    if len(especulada) != num_letras:
        print("\n    Apenas palavras de {0} letras".format(num_letras))
        continue
    #Quando a palavra não está na lista de palavras
    elif especulada not in base_palavras:
        print("\n    Palavra desconhecida")
        continue

    print("\n    INSPER :: TERMO")

    #Devolve a palavra especulada com a senha de cores
    resposta = senha_cores(sorteada,especulada)
    # Devolve a palavra especulada colorida e separada por barras

    print("    --- --- --- --- --- ")
    print("    " + resposta)
    print("    --- --- --- --- --- ")
    

    #Quando acerta a resposta       
    if resposta == sorteada:
        print("\n    >>> Parabéns! Você acertou a palavra!")
        jogo_novo = input("Jogar novamente? [s|n] ")

        #Sair do jogo
        if jogo_novo.lower() == "n":
            break
        #Iniciar novo jogo
        elif jogo_novo.lower() == "s":
            num_letras = int(input("\n    Quantas letras na palavra? "))
            tentativas = num_letras + 1
            print("\n    Sorteando uma palavra...")
            lista_palavras = filtra(base_palavras,num_letras)     #Cria lista de palavras com 5 letras
            dicionario = inicializa(lista_palavras)               #Cria dicionario
            sorteada = dicionario['sorteada']                     #Escolhe palavra sorteada aleatoriamente
            print("    Já tenho uma palavra! Tente adivinhá-la!")
    
    #Reduz uma tentativa
    tentativas -= 1

    #Caso o número de tentativas chegue a zero
    if tentativas == 0:
        print("\n    >>> Você perdeu, a palavra era: {0}".format(sorteada))
        jogo_novo = input("Jogar novamente? [s|n] ")

        #Sair do jogo
        if jogo_novo.lower() == "n":
            break
        #Iniciar novo jogo
        elif jogo_novo.lower() == "s":
            num_letras = int(input("\n    Quantas letras na palavra? "))
            tentativas = num_letras + 1
            print("\n    Sorteando uma palavra...")
            lista_palavras = filtra(base_palavras,num_letras)     #Cria lista de palavras com 5 letras
            dicionario = inicializa(lista_palavras)               #Cria dicionario
            sorteada = dicionario['sorteada']                     #Escolhe palavra sorteada aleatoriamente
            print("    Já tenho uma palavra! Tente adivinhá-la!")

    print("\n    Você tem {0} tentaviva(s)".format(tentativas))

    
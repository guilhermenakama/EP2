
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
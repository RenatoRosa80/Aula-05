# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

try:

    letra = input(" Digite uma letra: ")
    letra = letra.upper()

    vogais = [ 'A', 'E', 'I', 'O', 'U' ]
    consoante = [ 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z', 'Y' ]

    if letra in vogais:
        print(" A letrta é uma Vogal! ")
    elif letra in consoante:
        print(" A letra é uma Consoante!")
    else:
        print(" O caracter digitado não é uma letra!")
    
    #print(letra)

    """
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        print(" A letra digitada é uma Vogal!")
    else:
        print(" É uma consoante!")
    """
except:
    print(" Digite somente vogal ou consoante! ")

   




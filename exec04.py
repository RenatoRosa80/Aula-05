# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

try:

    letra = input(" Digite uma letra: ")
    letra = letra.upper()
    
    #print(letra)

    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        print(" A letra digitada é uma Vogal!")
    else:
        print(" É uma consoante!")
except:
    print(" Digite somente vogal ou consoante! ")





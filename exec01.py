# 1. Faça um Programa que peça dois números e imprima o maior deles.

try:
    num1 = int(input(" Digite um número: "))
    num2 = int(input(" Digite o segundo número: "))
    if num1 > num2 :
        print("O maior número é" ,num1)
    elif num2 > num1:
        print("O maior é: " ,num2)
    else:
        print(" Os números sao iguais.")
    

except:
    print(" Digite um valor numérico: " )
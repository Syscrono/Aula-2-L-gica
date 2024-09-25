# Verificar Par ou Ímpar e Positivo ou Negativo:
# Escreva um programa que peça um número e use if para verificar
# se ele é par ou ímpar e também se é positivo ou negativo.

num = int(input("Digite o número: "))

if num % 2 == 0 and num > 0:
    print("O número é par e positivo")

elif num % 2 != 0 and num > 0:
    print("O número é impar e positivo")

elif num % 2 == 0 and num < 0:
    print("O número é par e negativo")

else:
    print("O número é impar e negativo")
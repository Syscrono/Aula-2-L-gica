# Verificação de Notas Aprovadas:
# Escreva um programa que peça duas notas de um aluno. Use operadores
# lógicos para verificar se as duas notas são maiores ou iguais a 6.

nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))

if nota1 < 6 and nota2 < 6:
    print("As duas notas são menores que 6")

else:
    if nota1 >=6 or nota2 >=6:
        print("Somente uma nota é maior ou igual a 6")

    else:
        if nota1 >= 6 and nota2 >= 6:
            print("As duas notas são maiores que 6")


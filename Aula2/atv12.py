# Verificar Classificação de IMC:
# Crie um programa que calcule o Índice de Massa Corporal (IMC)
# e use if para classificar o resultado em "Abaixo do peso",
# "Peso normal", "Sobrepeso" e "Obesidade".

peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

resultado = round(peso / (altura ** 2),0)

print(resultado)
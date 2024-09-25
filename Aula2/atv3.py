# Atividade 03:
# Verificação de Maioridade e Habilitação:
# Crie um programa que peça a idade do usuário e se ele possui habilitação
# (sim ou não). Use operadores lógicos para verificar se ele é maior de idade
# (>= 18) e possui habilitação.


idade = int(input("Digite dua idade: "))
cnh = input("Você possui CNH: ")

if idade >= 18 and cnh == 'sim':
    print("Você é maior de idade e possui CNH")

else:
    if idade >= 18 and cnh == 'não':
        print("Você é maior de idade mas não possui CNH")

    else:
        if idade < 18:
            print("Você é menor de idade")
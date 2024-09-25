# Sistema de Login Simples:
# Desenvolva um programa que peça ao usuário um nome de usuário e uma senha e 
# use if para verificar se são iguais a "admin" e "1234" , respectivamente.

usuario = input("Digite seu nome de usuário: ")
senha = int(input("Digite sua senha: "))

usuarioPadrao = "admin"
senhaPadrao = 1234

if usuario == usuarioPadrao and senha == senhaPadrao:
    print("Usuário e Senha Conferem")

else:
    print("Usuário ou Senha Não Conferem")
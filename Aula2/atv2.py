# Verificar Igualdade de Strings:
# Peça ao usuário duas palavras e use operadores
# de comparação para verificar se elas são iguais.

palavra1 = input('Digite a 1ª palavra: ')
palavra2 = input('Digite a 2ª palavra: ')

if palavra1.upper() == palavra2.upper():
    print(f'As palavras "{palavra1}" e "{palavra2}" são iguais.')
else:
    print(f'As palavras "{palavra1}" e "{palavra2}" são diferentes.')
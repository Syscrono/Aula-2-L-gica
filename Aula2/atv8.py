# Verificação de Palavras em uma Frase:
# Peça ao usuário para inserir uma frase e uma palavra.
# Use in para verificar se a palavra está na frase.

frase1 = input("Escvreva uma frase: ")
resultado = "aprovado" in (frase1.lower())

print(resultado)
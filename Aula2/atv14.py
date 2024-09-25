# Verificar Status de Taxa de Desconto:
# Crie um programa que peça ao usuário o preço original de um produto e
# a quantidade comprada. Use if para verificar se a quantidade é maior que
# 10 para aplicar um desconto de 10% sobre o total.

preco_original = float(input("Digite o preço original: "))
qnt_comprada = float(input("Digite a quantidade comprada: "))
desconto = 1 - (10 / 100)

if qnt_comprada > 10:
    print("O valor da compra com DESCONTO foi de: R$", preco_original * qnt_comprada * desconto)

else:
    print("O valor da compra sem DESCONTO foi de: R$", preco_original * qnt_comprada)
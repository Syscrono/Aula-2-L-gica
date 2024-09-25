# Desconto em Preço:
# Peça ao usuário para inserir o preço de um produto e, em seguida,
# use o operador de atribuição -= para aplicar um desconto de 5%.

preço = float(input("Digite o valor do produto: "))

preço -= (preço * 5/100)

print(preço)

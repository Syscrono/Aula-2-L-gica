# Comparação de Idades:
# Peça ao usuário duas idades e use operadores de comparação para
# verificar se a primeira idade é maior, menor ou igual à segunda.

idade1 = int(input("Informe a 1ª idade: "))
idade2 = int(input("Informe a 2ª idade: "))

if idade1 == idade2:
    print(f"A 1ª idade {idade1} e a 2ª idade {idade2} são iguais")
elif idade1 > idade2:
     print(f"A 1ª idade {idade1}, é maior que a 2ª idade informada, {idade2}")
else:
     print(f"A 1ª idade {idade1}, é menor que a 2ª idade informada, {idade2}")

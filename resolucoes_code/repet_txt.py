# Entrada de dados
palavra = input("Digite uma palavra: ")

# Verificação de palíndromo
if palavra == palavra[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")

# Entrada de dados
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Operação (exemplo: soma)
soma = num1 + num2

print("Resultado da soma:", soma)

numero = int(input("Digite um número inteiro: "))

# Verificação
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

print("Média das notas:", round(media, 2))

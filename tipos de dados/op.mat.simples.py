# Solicita um número do usuário
num1 = float(input("Digite o primeiro número: "))

# Realiza uma operação simples (soma, subtração, multiplicação, divisão)
operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

# Solicita outro número do usuário
num2 = float(input("Digite o segundo número: "))


if operacao == '+':
    print(num1 + num2)
elif operacao == '-':
    print(num1 - num2)
elif operacao == '*':
    print(num1 * num2)
elif operacao == '/':
    print(num1 / num2)
else:
    print("Operaçã inválida")


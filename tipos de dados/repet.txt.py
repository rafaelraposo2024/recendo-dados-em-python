# Solicita uma string e um número inteiro do usuário
texto = input("Digite uma string: ")
repeticoes = int(input("Digite um número inteiro: "))

# Repete a string o número de vezes informado, adicionando espaço entre as repetições
resultado = (texto + " ") * repeticoes

# Remove o espaço extra ao final da string
resultado = resultado.strip()

# Exibe o resultado
print("Resultado:", resultado)


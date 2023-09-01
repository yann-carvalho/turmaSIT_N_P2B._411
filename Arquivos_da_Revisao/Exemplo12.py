def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

numero = int(input("Informe um valor...: "))
resultado = calcular_fatorial(numero)
print("O fatorial de", numero, "é:", resultado)

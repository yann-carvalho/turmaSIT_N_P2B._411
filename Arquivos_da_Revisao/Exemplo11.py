def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = 15
if eh_par(numero):
    print(numero, "é um número par.")
else:
    print(numero, "não é um número par.")

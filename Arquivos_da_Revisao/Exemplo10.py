def calcular_media2(lista):
    soma = sum(lista)
    media = soma / len(lista)
    print("A média é:", media)

def calcular_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return media

numeros = [10, 20, 30, 40, 50]
media = calcular_media(numeros)
print("A média é:", media)
print("===================")
calcular_media2(numeros)

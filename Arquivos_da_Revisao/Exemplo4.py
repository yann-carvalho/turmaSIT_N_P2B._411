numeros = [5, 10, 15, 20, 25]
soma = 0
somapar = 0
for numero in numeros:
    if (numero%2==0):
        somapar += numero
    soma += numero

print(f"A soma dos números é........: {soma}")
print(f"A soma dos números pares é..: {somapar}")
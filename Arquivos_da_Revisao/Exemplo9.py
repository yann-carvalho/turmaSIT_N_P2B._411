# Criando uma lista inicial
frutas = ["maçã", "banana", "laranja", "uva"]

# Adicionando um item à lista
frutas.append("morango")

# Procurando um item na lista
if "banana" in frutas:
    print("Encontrou a banana na lista.")
else:
    print("Não encontrou a banana na lista.")

# Classificando a lista em ordem alfabética
frutas.sort()

# Removendo um item da lista
frutas.remove("laranja")

# Exibindo a lista final
print("Lista de frutas:", frutas)

texto = ""
frase = input("Digite uma frase: ")
print("Você digitou: {}".format(frase))
for palavra in frase.split(" "):
    texto += palavra[::-1]+" "
print('A frase informada invertida fica: {}'.format(texto))
palavra = input("Digite uma palavra: ")

vogais = 0
espacos = 0

for i in palavra:
    for j in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        if i == j:
            vogais = vogais + 1
    if i == " ":
        espacos = espacos + 1

print("Tem", vogais, "Vogais")
print("Tem", espacos,"Espacos")
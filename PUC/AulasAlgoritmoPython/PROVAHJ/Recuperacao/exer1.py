playerVida = int(input("Insira a vida de seu personagem: "))

if playerVida <= 100 and playerVida >= 0:
    if playerVida >= 80:
        print("Verde")
    elif playerVida >= 40 and playerVida < 80:
        print("Laranja")
    elif playerVida > 0 and playerVida < 40:
        print("Vermelho")
    else:
        print("Cinza")
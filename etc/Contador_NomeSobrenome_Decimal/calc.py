from alfabeto import *
from main import nameSur

# Listas
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
          "S", "T", "U", "V", "W", "X", "Y", "Z"]

def start(nameSur):
    letra = nameSur.split()
    junto = ''.join(letra)
    return junto

def calc_alfabeto(letters, spaces):
    for word in nameSur:
        switcher = {
            'a' or 'A': letraA,
            'b' or 'B': letraB,
            'c' or 'B': letraC,
            'd' or 'B': letraD,
            'e' or 'B': letraE,
            'f' or 'B': letraF,
            'g' or 'B': letraG,
            'h' or 'B': letraH,
            'i' or 'B': letraI,
            'j' or 'B': letraJ,
            'k' or 'B': letraK,
            'l' or 'B': letraL,
            'm' or 'B': letraM,
            'n' or 'B': letraN,
            'o' or 'B': letraO,
            'p' or 'B': letraP,
            'q' or 'B': letraQ,
            'r' or 'B': letraR,
            's' or 'B': letraS,
            't' or 'B': letraT,
            'u' or 'B': letraU,
            'v' or 'B': letraV,
            'w' or 'B': letraW,
            'x' or 'B': letraX,
            'y' or 'B': letraY,
            'z' or 'B': letraZ,
            ' ': nonLetra
            # default: print("ERROR: Incorrect Character") 
        }
    for word in nameSur:
        for letter in letras:
            if word == letter:
                letters += 1
                return letters
        if word == " ":
            spaces += 1
            return spaces

    print("\nTem", letters, "letras.")
    print("Tem", spaces, "espacos.")
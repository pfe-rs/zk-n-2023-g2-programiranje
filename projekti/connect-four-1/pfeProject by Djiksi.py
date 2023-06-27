print("Dobrodosli u Connect 4! 🔴🔵⚪")

def napraviMatricu():
    matrica = []
    for _ in range(6):
        red = [' '] * 7
        matrica.append(red)
    return matrica

def prikazi(matrica):
    for red in matrica:
        print('|'.join(red))
        print('-' * 15)

def popuni_kolonu(matrica, kolona, disk):
    for red in range(5, -1, -1):
        if matrica[red][kolona] == ' ':
            matrica[red][kolona] = disk
            return True
    return False

def pobedaBool(matrica, disk):
    if any(all(matrica[red][kolona + i] == disk for i in range(4)) for red in range(6) for kolona in range(4)):
        return True
    
    if any(all(matrica[red + i][kolona] == disk for i in range(4)) for red in range(3) for kolona in range(7)):
        return True
    if any(all(matrica[red + i][kolona + i] == disk for i in range(4)) for red in range(3) for kolona in range(4)):
        return True

    if any(all(matrica[red - i][kolona + i] == disk for i in range(4)) for red in range(3, 6) for kolona in range(4)):
        return True

    return False

def main():
    matrica = napraviMatricu()
    diskTr = 'X'
    brPoteza = 0

    while True:
        prikazi(matrica)

        if diskTr == 'X':
            takmicar = "Prvi takmičar"
        else:
            takmicar = "Drugi takmičar"

        print(f"\nNa potezu je {takmicar}.")
        kolona = int(input("Unesite broj kolone (1-6): "))

        if kolona < 1 or kolona > 7:
            print("Pogrešan unos! Unesite broj kolone (1-7).")
            continue

        if not popuni_kolonu(matrica, kolona, diskTr):
            print("Kolona je puna! Pokušajte ponovo.")
            continue

        if pobedaBool(matrica, diskTr):
            prikazi(matrica)
            print(f"\n{takmicar} je pobedio!")
            break

        brPoteza += 1

        if brPoteza == 42:
            prikazi(matrica)
            print("\nIgra je završena. Nerešeno!")
            break

        diskTr = 'O' if diskTr == 'X' else 'X'

main()
def prikazi(matrica):
    for red in matrica:
        print("|", end=" ")
        for polje in red:
            print(polje, end=" ")
        print("|")
    print("-----------------------------")
    print("  1 2 3 4 5 6 7")

def moze(matrica, kolona):
    return matrica[0][kolona] == " "

def igraj(matrica, kolona, igrac):
    for red in range(5, -1, -1):
        if matrica[red][kolona] == " ":
            matrica[red][kolona] = igrac
            break

def pobedaBool(matrica, igrac):
    for red in range(6):
        for kolona in range(4):
            if matrica[red][kolona] == matrica[red][kolona+1] == matrica[red][kolona+2] == matrica[red][kolona+3] == igrac:
                return True

    for red in range(3):
        for kolona in range(7):
            if matrica[red][kolona] == matrica[red+1][kolona] == matrica[red+2][kolona] == matrica[red+3][kolona] == igrac:
                return True

    for red in range(3):
        for kolona in range(4):
            if matrica[red][kolona] == matrica[red+1][kolona+1] == matrica[red+2][kolona+2] == matrica[red+3][kolona+3] == igrac:
                return True

    for red in range(3, 6):
        for kolona in range(4):
            if matrica[red][kolona] == matrica[red-1][kolona+1] == matrica[red-2][kolona+2] == matrica[red-3][kolona+3] == igrac:
                return True

    return False

def main():
    matrica = [[" " for _ in range(7)] for _ in range(6)]
    trIgrac = "X"

    while True:
        prikazi(matrica)
        print("Red je na igrača", trIgrac)

        kolona = int(input("Unesite broj kolone (1-7): ")) - 1

        if kolona < 0 or kolona >= 7:
            print("Pogrešan unos! Pokušajte ponovo.")
            continue

        if not moze(matrica, kolona):
            print("Kolona je puna! Pokušajte ponovo.")
            continue

        igraj(matrica, kolona, trIgrac)

        if pobedaBool(matrica, trIgrac):
            prikazi(matrica)
            print("Igrač", trIgrac, "je pobedio")
            break
        
        if trIgrac == "X":
            trIgrac = "O"
        else:
            trIgrac = "X"


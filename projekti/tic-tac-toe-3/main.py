

def main():
    uvoduigru = uvod ()
    tabla = napravi_tabelu()
    linijce = napravi_linijce(tabla)
    igrac_1 = 'X'
    igrac_2 ='O'
    puna_tabla = da_li_je_puna (tabla, igrac_1, igrac_2)
    


def uvod ():
# uvod u igru(pravila).
    print("Zdravo!Dobrodosli u igru.")
    print("\n")
    print("Pravila: Igrac jedan je X,a drugi igrac je O. "
          "Potrebno je da uneste zeljeno mjesto u tabli,i "
          "igrac koji prvi uspije da popuni tri uzastopna polja vertikalno,horizontalno ili dijagonalno,pobjedjuje.")
    print("\n")
    

def napravi_tabelu():
# Ova funkcija pravi tabelu za igru
    print("Ovo je tabla na kojoj igrate.Srecno! ")
    tabla = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return tabla


def pocni_igru(tabla, igrac_1, igrac_2, brojac):
# ovde pocinje igra

    if brojac % 2 == 0:
        igrac = igrac_1
    elif brojac % 2 == 1:
        igrac = igrac_2
    print("Igrac "+ igrac + ", Vas je red.")
    row = int(input("Izaberite red,ako zelite:"
                    "gornji red unesite 0,srednji red unesite 1,donji red unesite 2:"))
    column = int(input("Izaberite kolonu,ako zelite:"
                       "lijevu kolonu unesite 0, srednju kolonu unesite 1, desnu kolonu unesite 2:"))


    # provjera da li su igraci unijeli pogresna mjesta(nepostojece koordinate)
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        van_table(row, column)
        row = int(input("Izaberite red,ako zelite:"
                        "gornji red unesite 0,srednji red unesite 1,donji red unesite 2:"))
        column = int(input("Izaberite kolonu,ako zelite"
                           "lijevu kolonu unesite 0, srednju kolonu unesite 1, desnu kolonu unesite 2:"))

        # provjera da li je polje puno(vec popunjeno)
    while (tabla[row][column] == igrac_1)or (tabla[row][column] == igrac_2):
        print("Polje(lokacija) u koju ste unijeli simbol je vec popunjena,molimo Vas da popunite drugo prazno polje!")
        row = int(input("Izaberite red,ako zelite:"
                        "gornji red unesite 0,srednji red unesite 1,donji red unesite 2:"))
        column = int(input("Izaberi kolonu,ako zelis"
                           "lijevu kolonu unesi 0, srednju kolonu unesi 1, desnu kolonu unesi 2:"))    
        
    # upisivanje znaka na polje
    tabla[row][column] = igrac
    return (tabla)

def da_li_je_puna(tabla, igrac_1, igrac_2):
    brojac = 0
    winner = False

    while brojac < 9 and winner == False:
        igra = pocni_igru(tabla, igrac_1, igrac_2, brojac)
        linijce = napravi_linijce (tabla)
        
        if brojac == 8:
            print("Tabla je puna, igra je gotova!")
            if winner == False:
                print("Nerjeseno!")

        # da li ima pobjednik
        winner = pobjednik(tabla, igrac_1, igrac_2, brojac)
        brojac += 1
    if winner == True:
        print("Kraj igre!")
        
    # ova funkcija vrsi vracanje
    report(brojac, winner, igrac_1, igrac_2)

# ova funkcija pokazuje igracima da su unijeli vrijednost van table
def van_table(row, column):
    print("Vrijednost koju ste unijeli je van polja.Molimo Vas da uneste opet vrijednost koja je vec data u uputstvu.")
    
def napravi_linijce(tabla):
# printa linije
    rows = len(tabla)
    cols = len(tabla)
    print("---+---+---")
    for r in range(rows):
        print(tabla[r][0], " |", tabla[r][1], "|", tabla[r][2])
        print("---+---+---")
    return tabla

def pobjednik(tabla, igrac_1, igrac_2, brojac):
# da li ima pobjednika
    winner = False
    # provjerava redove
    for row in range (0, 3):
        if (tabla[row][0] == tabla[row][1] == tabla[row][2] == igrac_1):
            winner = True
            print("Igrac " + igrac_1 + ", pobjedili ste!")
   
        elif (tabla[row][0] == tabla[row][1] == tabla[row][2] == igrac_2):
            winner = True
            print("Igrac " + igrac_2 + ", pobjedili ste!")


# provjerava kolone 
    for col in range (0, 3):
        if (tabla[0][col] == tabla[1][col] == tabla[2][col] == igrac_1):
            winner = True
            print("Igrac " + igrac_1 + ", Vi ste pobjedili!")
        elif (tabla[0][col] == tabla[1][col] == tabla[2][col] == igrac_2):
            winner = True
            print("Igrac " + igrac_2 + ", Vi ste pobjednik")

    # provjerava dijagonale
    if tabla[0][0] == tabla[1][1] == tabla[2][2] == igrac_1:
        winner = True
        print("Igrac " + igrac_1+ ", Vi ste pobjedili!")

    elif tabla[0][0] == tabla[1][1] == tabla[2][2] == igrac_2:
        winner = True
        print("Igrac " + igrac_2 + ", Vi ste pobjedili!")

    elif tabla[0][2] == tabla[1][1] == tabla[2][0] == igrac_1:
        winner = True
        print("Igrac " + igrac_1 + ", Vi ste pobjednik")

    elif tabla[0][2] == tabla[1][1] == tabla[2][0] == igrac_2:
        winner = True
        print("Igrac " + igrac_2 + ", Vi ste pobjednik")

    return winner

def report(brojac, winner, igrac_1, igrac_2):
    print("\n")
    input("Pritisnite enter,da vidite ishod igre.")
    if (winner == True) and (brojac % 2 == 1 ):
        print("Pobjednik: Igrac " + igrac_1 + ".")
    elif (winner == True) and (brojac % 2 == 0 ):
        print("Pobjednik: Igrac " + igrac_2 + ".")
    else:
        print("Nerjeseno! ")

# pozivamo funkciju main()
main()













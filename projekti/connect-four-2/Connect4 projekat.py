tabla = [[" "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "]]

def printConect4():
    for x in range(6):
        print("\n   |---|---|---|---|---|---|---|")
        print(x, " |", end="")
        for y in range(7):
            if(tabla[x][y] == "X"):
                print("", tabla[x][y], end=" |")
            elif(tabla[x][y]=="O"):
                print("", tabla[x][y], end=" |")
            else:
                print("", tabla[x][y], end=" |")
    print("\n   |---|---|---|---|---|---|---|")

print("Dobrobošli u igru Connect 4. To je jedna uzbudljiva igra u kojoj da bi pobedio, potrebno je da složiš četri ista znaka u redu u tablici - horizontalno, vertikalno ili dijagonalno. Pravo je vreme da pokažete svoju oštroumnost. Srećno!")
printConect4()
prvi_igrac=input("Igraču broj jedan unesite svoje ime:")
drugi_igrac=input("Igraču broj dva unesite svoje ime:")
true=1
for j in range(6*7):
    if j % 2 == 0:
        print("Na potezu je", prvi_igrac)
        igrac1=int(input( "Ubacite svoj žeton u željenu kolonu (1-6)."))
        for i in range(6):
            if tabla[5-i][igrac1]==" ":
                tabla[5-i][igrac1]="X"
                break
            if tabla[0][igrac1]=="X" or tabla[0][igrac1]=="O":
                print("Ta kolona je popunjena, molimo Vas ubacite žeton u neku drugu.")
                igrac1=int(input( "Ubacite svoj žeton u željenu kolonu."))
                for i in range(6):
                    if tabla[5-i][igrac1]==" ":
                        tabla[5-i][igrac1]="X"
                        break
                break
                        
        while true==1:       
            for y in range(6):
                for x in range(3):
                    if (tabla[x][y]=="X" and tabla[x+1][y]=="X" and tabla[x+2][y]=="X" and tabla[x+3][y]=="X"):
                        true=0
            for x in range(6):
                for y in range(4):
                    if (tabla[x][y]=="X" and tabla[x][y+1]=="X" and tabla[x][y+2]=="X" and tabla[x][y+3]=="X"):
                        true=0
            for x in range(3):
                for y in range(3,7):
                    if (tabla[x][y]=="X" and tabla[x+1][y-1]=="X" and tabla[x+2][y-2]=="X" and tabla[x+3][y-3]=="X"):
                        true=0
            for x in range(3):
               for y in range(4):
                    if (tabla[x][y]=="X" and tabla[x+1][y+1]=="X" and tabla[x+2][y+2]=="X" and tabla[x+3][y+3]=="X"):
                        true=0
            printConect4()
            break
    
    
    else:
        print("Na potezu je", drugi_igrac)
        igrac2=int(input("Ubacite svoj žeton u željenu kolonu."))
        for i in range(6):
            if tabla[5-i][igrac2]==" ":
                tabla[5-i][igrac2]="O"
                break
            if tabla[0][igrac2]=="O" or tabla[0][igrac2]=="X":
                print("Ta kolona je popunjena, molimo Vas ubacite žeton u neku drugu.")
                igrac2=int(input("Ubacite svoj žeton u željenu kolonu (1-6)."))
                for i in range(6):
                    if tabla[5-i][igrac2]==" ":
                        tabla[5-i][igrac2]="O"
                        break
                break
                    
        while true == 1:
            for y in range(6):
                for x in range(3):
                    if (tabla[x][y]=="O" and tabla[x+1][y]=="O" and tabla[x+2][y]=="O" and tabla[x+3][y]=="O"):
                        true=3
            for x in range(6):
                for y in range(4):
                    if (tabla[x][y]=="O" and tabla[x][y+1]=="O" and tabla[x][y+2]=="O" and tabla[x][y+3]=="O"):
                        true=3
            for x in range(3):
                for y in range(3,7):
                    if (tabla[x][y]=="O" and tabla[x+1][y-1]=="O" and tabla[x+2][y-2]=="O" and tabla[x+3][y-3]=="O"):
                        true=3
            for x in range(3):
                for y in range(4):
                    if (tabla[x][y]=="O" and tabla[x+1][y+1]=="O" and tabla[x+2][y+2]=="O" and tabla[x+3][y+3]=="O"):
                        true=3

            printConect4()
            break
    if true==0:
        print("Kraj igre! Čestitamo, pobednik je", prvi_igrac)
        break
    if true==3:
        print("Kraj igre! Čestitamo pobednik je", drugi_igrac)
        break
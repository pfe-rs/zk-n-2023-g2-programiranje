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

prvi_igrac=input("Igraču broj jedan unesite svoje ime:")
drugi_igrac=input("Igraču broj dva unesite svoje ime:")
true=1
for j in range(21):
    if j % 2 == 0:
        while true==1:
            print("Sledeći potez ima", prvi_igrac)
            igrac1=int(input( "Ubacite svoj žeton u željenu kolonu."))
            for i in range(6):
                if tabla[5-i][igrac1]==" ":
                    tabla[5-i][igrac1]="X"
                    break
  
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
                        break
            for x in range(3):
                for y in range(4):
                    if (tabla[x][y]=="X" and tabla[x+1][y+1]=="X" and tabla[x+2][y+2]=="X" and tabla[x+3][y+3]=="X"):
                        true=0
                        break
            print(tabla)
            printConect4()
            break
    
    
    else:
        while true==1:
            print("Sledeći potez ima", drugi_igrac)
            igrac2=int(input("Ubacite svoj žeton u željenu kolonu."))
            for i in range(6):
                if tabla[5-i][igrac2]==" ":
                    tabla[5-i][igrac2]="O"
                    break
  
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
                        break
            for x in range(3):
                for y in range(4):
                    if (tabla[x][y]=="O" and tabla[x+1][y+1]=="O" and tabla[x+2][y+2]=="O" and tabla[x+3][y+3]=="O"):
                        true=3
                        break
            break
           
        print(tabla)
        printConect4()
    if true==0:
        print("Kraj igre! Čestitamo, pobednik je", prvi_igrac)
        break
    if true==3:
        print("Kraj igre! Čestitamo pobednik je", drugi_igrac)
        break
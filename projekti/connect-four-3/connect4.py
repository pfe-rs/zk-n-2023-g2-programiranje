tabla = [[" ", " ", " ", " ", " ", " ", " ",],
         [" ", " ", " ", " ", " ", " ", " ",],
         [" ", " ", " ", " ", " ", " ", " ",],
         [" ", " ", " ", " ", " ", " ", " ",],
         [" ", " ", " ", " ", " ", " ", " ",],
         [" ", " ", " ", " ", " ", " ", " ",]]
kraj = 0
ind = [5, 5, 5, 5, 5, 5, 5]
igrac = 1
znak = "X"
while kraj==0:
    for i in range(6):
        print(tabla[i])
    nzm=0
    for pro in range(7):
        if(ind[pro]!=-1):
            nzm=1
    if nzm==0:
        kraj=0
        print("Nereseno!")
        for i in range(6):
            print(tabla[i])
        continue
    j = int(input("Uneti broj kolone u koji zelite ubaciti zeton: "))
    if j>6:
        j = int(input("Mozete uneti iskljucivo kolone 0-6. Broj kolone: "))
    while ind[j]==-1:
        j = int(input("Uneta kolona je puna, izaberite drugu: "))
    if igrac == 1:
        tabla[ind[j]][j]="X"
        igrac = 2
        znak = "X"
    else:
        tabla[ind[j]][j]="O"
        igrac = 1
        znak = "O"
    br=0
    for i in range(ind[j],6):
        if br==4:
            print("Pobedio je "+znak+" igrac. ")
            for i in range(6):
                print(tabla[i])
            kraj=1
        if tabla[i][j]==znak: #po koloni
            br+=1
        else:
            break
    if br==4:
            print("Pobedio je "+znak+" igrac. ")
            for i in range(6):
                print(tabla[i])
            kraj=1
    br=0
    k=ind[j]
    for i in range(7):
        if br==4:
            print("Pobedio je "+znak+" igrac. ")
            for i in range(6):
                print(tabla[i])
            kraj=1
        if tabla[k][i]==znak: #po vrsti
            br+=1
        else:
            br=0
    if br==4:
            print("Pobedio je "+znak+" igrac. ")
            for i in range(6):
                print(tabla[i])
            kraj=1
    ind[j]-=1 
    ii=3
    jj=0
    for g in range(3):
        for h in range(0,4):
            if(tabla[ii+g][jj+h]==znak and tabla[ii+g-1][jj+h+1]==znak and tabla[ii-2+g][jj+h+2]==znak and tabla[ii-3+g][jj+h+3]==znak):
                kraj=1
                print("Pobedio je "+znak+" igrac. ")
                for i in range(6):
                    print(tabla[i])
                break
    ii=2
    jj=0
    for g in range(3):
        for h in range(4):
            if(tabla[ii-g][jj+h]==znak and tabla[ii-g+1][jj+h+1]==znak and tabla[ii-g+2][jj+h+2]==znak and tabla[ii-g+3][jj+h+3]==znak):
                kraj=1
                print("Pobedio je "+znak+" igrac. ")
                for i in range(6):
                    print(tabla[i])
                break
    
                
                
                
                
                
    

import random
tvoja_rec=str
list=['enciklopedija','igračka','telefon','pisac','euforija','laptop','dioda','tranzistor','elektronika']
tvoja_rec=random.choice(list)
pogodak=["_"]*len(tvoja_rec)
br_greska=0
kraj = False
brzi_pogodak=str
rec=str
while not kraj :
    print(pogodak)
    slovo=str(input("Pogodi slovo: "))
    print(slovo)
    ok = False


    for i in range(len(tvoja_rec)):
        if tvoja_rec[i]==slovo:  
            pogodak[i]=slovo
            print(pogodak)
            
            print("Čestitam pogodili ste slovo")
            ok=True
            brzi_pogodak=str(input("Da li mozete da pogodite celu rec,odgovovori sa da/ne? "))
            if brzi_pogodak=="ne":
                break
            elif brzi_pogodak=="da":
                rec=str(input("Unesite vasu rec "))
                if rec==tvoja_rec:
                    print("Čestitam pogodili ste rec")
                    kraj=True

                elif rec!=tvoja_rec:
                    print("Nažalost nisi u pravu  ali možeš da nastaviš!")
                continue



    if not ok:
        print("Greška,probajte ponovo")
        br_greska=br_greska + 1
        if br_greska>=5:  
           print("Žao mi je ,izgubio si")
           kraj=True
        
        continue
        
        
       # if not ok:
           # br_greska=br_greska + 1
           #
           # print("Greška,probajte ponovo")
       # if br_greska>=5:  
           # print("Žao mi je ,izgubio si")
           # kraj=True 
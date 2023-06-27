import random
 
vesalo_slike = [
    """
      +---+
          |
          |
          |
         ===
    """,
    """
      +---+
      O   |
          |
          |
         ===
    """,
    """
      +---+
      O   |
      |   |
          |
         ===
    """,
    """
      +---+
      O   |
     /|   |
          |
         ===
    """,
    """
      +---+
      O   |
     /|\  |
          |
         ===
    """,
    """
      +---+
      O   |
     /|\  |
     /    |
         ===
    """,
    """
      +---+
      O   |
     /|\  |
     / \  |
         ===
    """
]
 
def vesalo():
    reci = ["duks", "grisine", "matematika", "informatika", "elektronika", "fizika", "program", "neznalac", "kontinent", "trenerka", "limenka", "kafa", "tetris", "pijaca", "kesa", "gramatka", "test", "jezik", "tastatura"]  
    rec = random.choice(reci)
    pokusaji = 6
    pogodjena_slova = []  
 
 
    while pokusaji > 0:
        for slovo in rec:
            if slovo in pogodjena_slova:
                print(slovo, end=" ")
            else:
                print("_", end=" ")
        print("\n")
 
        pogodak = input("Pogodi slovo!: ").lower()
        if len(pogodak) != 1:
            print("Upisi jedno slovo, a ne vise slova.")
            continue
   
        if pogodak in pogodjena_slova:
            print("Vec ste izabrali ovo slovo. Izaberite drugo.")
            continue
       
        pogodjena_slova.append(pogodak)
 
        if pogodak in rec:
            print("Tacno slovo!")
        elif not pogodak.isalpha():
            print("Unesi odgovarajuci simbol.")    
        else:
            print("Ovo slovo se ne sadrzi u reci.")
            pokusaji -= 1
            print(vesalo_slike[6 - pokusaji])
            print("Ostalo ti je jos", pokusaji, "pokusaja.")
 
        nalazenje_reci = all(slovo in pogodjena_slova for slovo in rec)
        if nalazenje_reci:
            print("Cestitamo, kraj igre")
            print("Pogodjena rec je bila:", rec)
            break
 
    if pokusaji == 0:
        print("Nazalost, izgubuli ste. :")
        print("Rec je bila", rec)
        
while True:
    vesalo()
    word = input("Zelite li opet da igrate igru (da/ne): ").lower()
    if word == "ne":
        break
    print("\n\n***NOVA IGRA***\n")

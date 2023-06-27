import random
lista_reci=["VUK","PLANINA","PROZOR","SELO","SPAVATI","JADNO","SMRAD","OCAJNO","OLUJA","AVALON","KONDENZATOR","INDUKTOR","OTPORNIK","KAFA"]
random_rec= random.choice(lista_reci)
i=0
correct_guess=0
zivoti=6
slovo=[]
for i in range(len(random_rec)):
    print(" _ ",end=" ")
while (correct_guess < len(random_rec) and zivoti > 0):
    guess=str(input("Guess: ")).upper()
    for i in range(len(random_rec)):
        if random_rec[i] == guess:
            print(" " + guess + " ",end=" ")
            correct_guess=correct_guess+1
        elif random_rec[i] in slovo: print(" " + random_rec[i] + " ",end=" ")
        elif len(guess)==1: print(" _ ",end=" ")
        else:
             print("Only one letter allowed. ")
             break
    if str(guess) in random_rec and len(guess)<2 :
        print("Good guess!")
        slovo.append(guess)
    elif len(guess)<2:
        zivoti=zivoti-1
        print("Wrong guess... " + str(zivoti) + " lives left.")
    else:
        zivoti=zivoti-1
        print("You typed more than one letter..." + str(zivoti) + " lives left.")
if correct_guess == len(random_rec):
    print("You win! The word was: " + random_rec)
elif zivoti == 0:
    print("You lost...The word was: " + random_rec)
print("Thanks for playing!")
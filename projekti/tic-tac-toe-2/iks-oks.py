import sys

  
def proveravanje_pobede(tabla):
    if( tabla[0][0]==tabla[0][1]==tabla[0][2] and tabla[0][0]!='N'):
      print("IGRAČ JE POBEDIO!")
      sys.exit()
    elif( tabla[1][0]==tabla[1][1]==tabla[1][2] and tabla[1][0]!='N'):
      print("IGRAČ JE POBEDIO!")
      sys.exit()
    elif( tabla[2][0]==tabla[2][1]==tabla[2][2] and tabla[2][0]!='N'):
      print("IGRAČ JE POBEDIO!")
      sys.exit()
    elif( tabla[0][0]==tabla[1][0]==tabla[2][0] and tabla[0][0]!='N'):
      print("IGRAČ JE POBEDIO!")
      sys.exit()
    elif( tabla[0][1]==tabla[1][1]==tabla[2][1] and tabla[0][1]!='N'):
      print("IGRAČ JE POBEDIO!")
      sys.exit()
    elif( tabla[0][2]==tabla[1][2]==tabla[2][2] and tabla[0][2]!='N'):
      print("IGRAČ JE POBEDIO!")
      sys.exit()
    elif( tabla[0][0]==tabla[1][1]==tabla[2][2] and tabla[0][0]!='N'):
      print("IGRAČ JE POBEDIO!")
      sys.exit()
    elif( tabla[0][2]==tabla[1][1]==tabla[2][0] and tabla[0][2]!='N'):
      print("igrac je pobedio")
      sys.exit()
      return True
    else:
      return False

    
  
import os
print (" ")
print (" ")
if __name__ == "__main__":  
   
      
    prvi_igrac = input("MOLIMO PRVOG IGRAČA DA UNESE SVOJE IME: ")  
    print("\n")  
    
    drugi_igrac = input("MOLIMO DRUGOG IGRAČA DA UNESE SVOJE IME:  ")  
    print("\n")  

    print("X(IKS) PRIPADA PRVOM IGRAČU, O(OKS) PRIPADA DRUGOM IGRACU.")



tabla = [['N', 'N', 'N'],
          [ 'N', 'N', 'N'], 
          ['N', 'N', 'N']]

for x in tabla:
  for y in x:
    for z in y:
      print(z ,end=' ')
  print('')
  

koordinata=-1
brojac=0
brojac2=0
while True:
  pun=0
  if(brojac2%2==0):
    print("PRVI IGRAČ JE NA REDU.")
    x=int(input(''))
    y=int(input(''))
    if(0<=x<=2 and 0<=y<=2): 
      if(tabla[x][y]=='N'):
        tabla[x][y]="x"
        brojac2+=1
      else:
        pun=1
    else:
      pun=1
  else:
    print("DRUGI IGRAC JE NA REDU.")
    x=int(input(''))
    y=int(input(''))
    if(0<=x<=2 and 0<=y<=2): 
      if(tabla[x][y]=='N'):
        tabla[x][y]="o"
        brojac2+=1
      else:
        pun=1
    else:
      pun=1

  os.system('cls')
  if(pun==1):
    print("UNOS NIJE PODRŽAN. UNESITE PONOVO.")
    pun=0
  brojac=0
  for i in range(3):
    for j in range(3):
      if(tabla[i][j]!='N'):
        brojac+=1
  if(brojac==9):
    print("REZULTAT JE NEREŠEN.")
    sys.exit()
  
 
  for x in tabla:
    for y in x:
      for z in y:
        print(z, end=' ')
    print('')
    provera=proveravanje_pobede(tabla)

    if(provera):
      break
   
   
 
   
  

  
 
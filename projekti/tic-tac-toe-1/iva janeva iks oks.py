i=0
n=0
m=0
A=[["-","-","-" ],
  [ "-","-" ,"-" ],
  [ "-","-" ,"-" ]]
  
pobeda = False
for i in range(5):
 if i==4:
     r= int(input (" Igrac 1 vnesi red kade sakas da stavis X "))
     k= int(input (" i kolona "))
     if A[r-1][k-1]=="-":
        
         A[r-1][k-1]="X"
        
         for n in range(3):
               if A[0][n]==A[1][n]==A[2][n]=="X" or A[n][0]==A[n][1]==A[n][2]=="X" or A[0][0]==A[1][1]==A[2][2]=="X" or A[0][2]==A[1][1]==A[2][0]=="X":
                print("Pobednik e prviot igrac")
                pobeda = True
                break
         if (pobeda== False) :
            print(" izigrafte nereseno ")
      
 else:
     igrac1 = True
     while(igrac1):
         r= int(input (" Igrac 1 vnesi red kade sakas da stavis X"))
         k= int(input (" i kolona "))
         if A[r-1][k-1]=="-":
            
             A[r-1][k-1]="X"
             for i in range(3):
              print(A[i], "\n ")
             for n in range(3):
                   if A[0][n]==A[1][n]==A[2][n]=="X" or A[n][0]==A[n][1]==A[n][2]=="X" or A[0][0]==A[1][1]==A[2][2]=="X" or A[0][2]==A[1][1]==A[2][0]=="X":
                    print("Pobednik e prviot igrac")
                    pobeda = True
                    break
             igrac1 = False     
         else:
             print("Toa mesto vo tabelata e vekje zafateno vnesi drugo mesto ")
             i-=1
             continue
     if pobeda == True:
         break
     
     igrac2 = True
     while(igrac2):
         r1= int(input (" Igrac 2 vnesi red kade sakas da stavis O "))
         k1= int(input (" i kolona "))
         if A[r1-1][k1-1]=="-":
               A[r1-1][k1-1]="O"
               for i in range(3):
                print(A[i], "\n ")
               
               for n in [0,1,2]:
                 if A[0][n]==A[1][n]==A[2][n]=="0" or A[n][0]==A[n][1]==A[n][2]=="0" or A[0][0]==A[1][1]==A[2][2]=="0" or A[0][2]==A[1][1]==A[2][0]=="0":
                  print("pobednik e vtoriot igrac")
                  pobeda = True
                  break
               igrac2 = False
         else:
             print("Toa mesto vo tabelata e vekje zafateno vnesi drugo mesto ")
     
     if pobeda == True:
        break    

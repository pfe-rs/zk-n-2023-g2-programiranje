import math

def sudaren(levo,gore,sirina,visina,centarx,centary,poluprecnik):
    klevo,kgore,kdesno,kdole=centarx-poluprecnik,centary-poluprecnik,centarx+poluprecnik,centary+poluprecnik
    desno,dole=levo+sirina,gore+visina
    
    if desno<klevo or levo>kdesno or dole<kgore or gore>kdole:
        return False
    
    for x in(levo,levo+sirina):
        for y in (gore,gore+visina):
            if math.hypot(x-centarx,y-centary)<=poluprecnik:
                return True
    if levo<=centarx<=desno and gore<=centary<=dole:
        return True
    return False


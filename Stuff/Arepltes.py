def arip(x):
    if x <= 2:
        return("kecil")
    elif x == 3:
        return("pas")
    else:
        return("gede")
    
nomor1 = int(input("masukan nomor : "))  

print(arip(nomor1))
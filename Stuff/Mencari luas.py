print("Mecari tau Luas dan keliling Segitiga\n")

Alas = int(input("Silahkan masukan Alas \t: "))
Tinggi = int(input("Silahkan masukan Tinggi : "))

Luas = 0.5 * Alas * Tinggi
Miringq2 = (Alas * Alas) + (Tinggi * Tinggi)
Miring = Miringq2 ** 0.5
Keliling = Miring + Alas + Tinggi

print("\nLuas dari Segitiga tersebut adalah \t: ", Luas, "cm2")
print("Keliling dari Segitiga tersebut adalah \t: " , Keliling, "cm")


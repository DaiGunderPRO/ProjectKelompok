import random

nomor_acak = random.randint(1,20)

print("coba tebak usia saya!")

while True:
    guess = int(input("usia saya adalah: "))

    if guess < nomor_acak:
        print("terlalu muda! coba lagi.")
    elif guess > nomor_acak:
        print("terlalu tua! coba lagi.")
    else:
        print("Betoel sekali!")
        break


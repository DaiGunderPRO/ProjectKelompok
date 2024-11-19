NamaSaya = "Nicholas Romanov"
KelasSaya = "15.1A.07"
JurusanSaya = "Informatika"
UsiaSaya = "21 thn"
HobbySaya = "Gaming & Coding"

print("===================================================")
print("Selamat Datang di perkenalan saya")
print("nama / kelas / jurusan / usia / hobby")
print("ketik (selesai) untuk keluar")
print("===================================================")

print("Apa yang mau ditanyakan")

while True:

 user_input = input("dari pilihan diatas?\t\t:")

 if user_input.lower() == "nama":
    print("===================================================")
    print("Nama saya adalah", NamaSaya)
    print("apalagi yang mau ditanyakan?")

 elif user_input.lower() == "kelas":
    print("===================================================")
    print("Saya berada di kelas", KelasSaya)
    print("apalagi yang mau ditanyakan")

 elif user_input.lower() == "jurusan":
    print("===================================================")
    print("Saya kuliah jurusan", JurusanSaya)
    print("apalagi yang mau ditanyakan")

 elif user_input.lower() == "usia":
    print("===================================================")
    print("Usia saya", UsiaSaya)
    print("apalagi yang mau ditanyakan")
  
 elif user_input.lower() == "hobby":
    print("===================================================")
    print("Hobby saya tentu", HobbySaya)
    print("apalagi yang mau ditanyakan")

 elif user_input.lower() == "selesai":
    print("===================================================")
    print("Terimakasih sudah meluangkan waktu untuk Menjalankan kode saya :) ")
    break
 else:
    print("===================================================")
    print("Maaf pilihan tersebut tidak termasuk di list")
    print("apalagi yang mau 3ditanyakan")

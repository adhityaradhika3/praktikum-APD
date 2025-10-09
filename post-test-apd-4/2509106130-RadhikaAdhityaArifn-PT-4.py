# Input stamina dari 3 digit terakhir NIM
stamina = int(input("Masukkan stamina  naruto: "))
chakra = 0

# Proses menyempurnakan Rasengan
while chakra < 200 and stamina > 0:
    chakra += 5
    stamina -= 3
    print("Chakra yang berhasil dikumpulkan:", chakra)
    print("Sisa stamina:", stamina)

if chakra >= 200:
    print("Naruto berhasil menyempurnakan Rasengan! ")
else:
    print("Naruto kehabisan stamina sebelum mencapai 200 chakra")

tinggi_menara = int(input("Masukkan tinggi menara (kelipatan 3): "))

jumlah_gulungan = 0
for ketinggian in range(3, tinggi_menara + 1, 3):
    jumlah_gulungan += 1

print("Jumlah gulungan informasi yang didapatkan Naruto:", jumlah_gulungan)
# Input jumlah koridor dari digit kedua terakhir NIM
jumlah_koridor = int(input("Masukkan jumlah koridor (digit kedua terakhir NIM): "))
intelijen = 300
perangkap = 0

# Proses penyelidikan
for koridor in range(1, jumlah_koridor + 1):
    for ruangan in range(1, 4):  # Setiap koridor memiliki 3 ruangan
        nomor_ruangan = (koridor - 1) * 3 + ruangan
        if nomor_ruangan % 2 == 1:
            intelijen += 1
        else:
            perangkap += 1

# Output hasil
print(f"Data Intelijen yang didapatkan: {intelijen}")
print(f"Perangkap Peledak yang berhasil dijinakkan: {perangkap}")
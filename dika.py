nama_pelanggan = input ("nama pelanggan :")
batu_bata = int(input ("jumlah batu bata: "))
semen = int(input ("jumlah semen: "))

harga_batu = 100
harga_semen = 100000
total = (batu_bata * harga_batu) + (semen * harga_semen)

paket_hemat = batu_bata == 500 and semen == 5
paket_ultra_mantap = batu_bata == 2000 and semen == 16

if paket_hemat :
    diskon = 0.15
    ket_diskon = "mendapatkan paket hemat"
elif paket_ultra_mantap :
    diskon = 0.30
    ket_diskon = "mendapatkan paket ultra mantap"
else:
    diskon = 0
    ket_diskon = "tidak mendapatkan diskon"

potongan_diskon = total * diskon
total_keseluruhan = total - potongan_diskon 


print("nama pelanggan :", nama_pelanggan)
print("jumlah batu bata :", batu_bata)
print("jumlah semen :", semen)
print("total sebelum diskon : Rp ", total)
print("diskon yang didapatkan : ", ket_diskon, int(diskon * 100), "%")
print("potongan diskon : Rp ", potongan_diskon)
print("biaya yang dibayarkan : Rp ", total_keseluruhan)




import os

users = {
    "admin": {"password": "130", "role": "admin"}
}

menu_padang = {
    "Rendang": 25000,
    "Ayam Pop": 20000,
    "Dendeng Balado": 22000,
    "Sayur Nangka": 10000,
    "Telur Dadar": 8000,
    "Sambal Hijau": 5000
}

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print("\n=== SISTEM WARUNG PADANG ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihan = input("Pilih: ")

    if pilihan == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN ===")
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username]["password"] == password:
            print(f"Login berhasil sebagai {users[username]['role']}")
            if users[username]["role"] == "admin":
                while True:
                    print("\n Menu Admin")
                    print("1. Lihat Menu")
                    print("2. Tambah Menu")
                    print("3. Hapus Menu")
                    print("4. Logout")
                    pilih_admin = input("Pilih: ")

                    if pilih_admin == "1":
                        print("\n Daftar Menu Warung Padang:")
                        for makanan, harga in menu_padang.items():
                            print(f"- {makanan}: Rp{harga}")
                    elif pilih_admin == "2":
                        nama = input("Nama makanan baru: ")
                        if nama in menu_padang:
                            print("Menu sudah ada.")
                        else:
                            harga = input("Harga: ")
                            if harga.isdigit():
                                menu_padang[nama] = int(harga)
                                print("Menu berhasil ditambahkan.")
                            else:
                                print("Harga harus berupa angka.")
                    elif pilih_admin == "3":
                        nama = input("Nama makanan yang ingin dihapus: ")
                        if nama in menu_padang:
                            del menu_padang[nama]
                            print("Menu berhasil dihapus.")
                        else:
                            print("Menu tidak ditemukan.")
                    elif pilih_admin == "4":
                        break
                    else:
                        print("Pilihan tidak valid.")
            else:
                pesanan = {}
                while True:
                    print(f"\n Menu Pengguna ({username})")
                    print("1. Lihat Menu")
                    print("2. Pesan Makanan")
                    print("3. Lihat Pesanan")
                    print("4. Logout")
                    pilih_user = input("Pilih: ")

                    if pilih_user == "1":
                        print("\n Daftar Menu Warung Padang:")
                        for makanan, harga in menu_padang.items():
                            print(f"- {makanan}: Rp{harga}")
                    elif pilih_user == "2":
                        nama = input("Nama makanan yang ingin dipesan: ")
                        if nama in menu_padang:
                            jumlah = input("Jumlah porsi: ")
                            if jumlah.isdigit():
                                if nama in pesanan:
                                    pesanan[nama] += int(jumlah)
                                else:
                                    pesanan[nama] = int(jumlah)
                                print(f"{jumlah} porsi {nama} ditambahkan.")
                            else:
                                print("Jumlah harus berupa angka.")
                        else:
                            print("Menu tidak tersedia.")
                    elif pilih_user == "3":
                        print("\n Pesanan Anda:")
                        total = 0
                        for item, qty in pesanan.items():
                            subtotal = menu_padang[item] * qty
                            print(f"- {item} x{qty} = Rp{subtotal}")
                            total += subtotal
                        print(f"Total Bayar: Rp{total}")
                    elif pilih_user == "4":
                        break
                    else:
                        print("Pilihan tidak valid.")
        else:
            print("Username atau password salah.")

    elif pilihan == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTRASI ===")
        username = input("Username baru: ")
        if username in users:
            print("Username sudah terdaftar.")
        else:
            password = input("Password: ")
            users[username] = {"password": password, "role": "user"}
            print("Registrasi berhasil!")

    elif pilihan == "3":
        print("Terima kasih telah berkunjung.")
        break
    else:
        print("Pilihan tidak valid.")
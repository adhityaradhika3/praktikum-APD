import os

users = {
    "Radhika": {"password": "130", "role": "admin"},
}
menu = {
    "Rendang": 25000,
    "Ayam Pop": 20000,
    "Dendeng Balado": 22000,
    "Sayur Nangka": 10000,
    "Telur Dadar": 8000,
    "Sambal Hijau": 5000
}
pesanan_user = {}

# === Fungsi Tanpa Parameter ===
def tampilkan_menu():
    print("\n--- Menu Warung Padang ---")
    for makanan, harga in menu.items():
        print(f"{makanan}: Rp{harga}")

def tampilkan_pengguna():
    print("\n--- Daftar Pengguna ---")
    for username, info in users.items():
        print(f"{username} ({info['role']})")

# === Fungsi Dengan Parameter ===
def tambah_menu(nama, harga):
    if nama in menu:
        print("Menu sudah ada.")
    else:
        menu[nama] = harga
        print(f"Menu '{nama}' berhasil ditambahkan.")

def pesan_makanan(nama, jumlah):
    if nama in menu:
        if nama in pesanan_user:
            pesanan_user[nama] += jumlah
        else:
            pesanan_user[nama] = jumlah
        print(f"{jumlah} porsi {nama} ditambahkan ke pesanan.")
    else:
        print("Menu tidak tersedia.")

# === Prosedur ===
def lihat_pesanan():
    print("\n--- Pesanan Anda ---")
    total = 0
    for item, qty in pesanan_user.items():
        subtotal = menu[item] * qty
        print(f"{item} x{qty} = Rp{subtotal}")
        total += subtotal
    print(f"Total Bayar: Rp{total}")

def registrasi():
    try:
        username = input("Username baru: ")
        if username in users:
            print("Username sudah terdaftar.")
            return
        password = input("Password: ")
        users[username] = {"password": password, "role": "user"}
        print("Registrasi berhasil!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# === Fungsi Rekursif ===
def konfirmasi_logout():
    jawaban = input("Yakin ingin logout? (y/n): ").lower()
    if jawaban == "y":
        return True
    elif jawaban == "n":
        return False
    else:
        print("Input tidak valid.")
        return konfirmasi_logout()

# === Program Utama ===
def main():

    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("\n=== SISTEM WARUNG PADANG ===")
        print("1. Login")
        print("2. Registrasi")
        print("3. Keluar")
        pilihan = input("Pilih: ")

        if pilihan == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            username = input("Username: ")
            password = input("Password: ")

            if username in users and users[username]["password"] == password:
                role = users[username]["role"]
                print(f"Login berhasil sebagai {role}")

                if role == "admin":
                    while True:
                        print("\n--- Menu Admin ---")
                        print("1. Lihat Menu")
                        print("2. Tambah Menu")
                        print("3. Lihat Pengguna")
                        print("4. Logout")
                        pilih_admin = input("Pilih: ")

                        if pilih_admin == "1":
                            tampilkan_menu()
                        elif pilih_admin == "2":
                            try:
                                nama = input("Nama makanan: ")
                                harga = int(input("Harga: "))
                                tambah_menu(nama, harga)
                            except ValueError:
                                print("Harga harus berupa angka.")
                        elif pilih_admin == "3":
                            tampilkan_pengguna()
                        elif pilih_admin == "4":
                            if konfirmasi_logout():
                                break
                        else:
                            print("Pilihan tidak valid.")
                else:
                    while True:
                        print("\n--- Menu Pengguna ---")
                        print("1. Lihat Menu")
                        print("2. Pesan Makanan")
                        print("3. Lihat Pesanan")
                        print("4. Logout")
                        pilih_user = input("Pilih: ")

                        if pilih_user == "1":
                            tampilkan_menu()
                        elif pilih_user == "2":
                            try:
                                nama = input("Nama makanan: ")
                                jumlah = int(input("Jumlah porsi: "))
                                pesan_makanan(nama, jumlah)
                            except ValueError:
                                print("Jumlah harus berupa angka.")
                        elif pilih_user == "3":
                            lihat_pesanan()
                        elif pilih_user == "4":
                            if konfirmasi_logout():
                                break
                        else:
                            print("Pilihan tidak valid.")
            else:
                print("Username atau password salah.")

        elif pilihan == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            registrasi()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem.")
            break
        else:
            print("Pilihan tidak valid.")

main()
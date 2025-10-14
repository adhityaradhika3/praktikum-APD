import os

# Data login awal
users = [['Radhika', '130', 'admin']]
# Data menu warung padang: [nama_menu, harga, kategori]
menu_warung = []
# Data pesanan: {username: [[nama_menu, jumlah, subtotal], ...]}
pesanan = {}

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== List Daftar Menu Warung Padang ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    # LOGIN
    if pilihan == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== Login ===")
        username = input("Username: ")
        password = input("Password: ")
        login_sukses = False
        for user in users:
            if user[0] == username and user[1] == password:
                login_sukses = True
                role = user[2]
                break
        if not login_sukses:
            print("Username atau password salah.")
            input("Tekan Enter untuk lanjut...")
            continue

        # MENU ADMIN
        while role == 'admin':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== Menu Admin Warung Padang ===")
            print("1. Lihat Menu")
            print("2. Tambah Menu")
            print("3. Ubah Menu")
            print("4. Hapus Menu")
            print("5. Logout")
            menu = input("Pilih menu: ")

            if menu == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== Daftar Menu ===")
                if len(menu_warung) == 0:
                    print("Belum ada menu.")
                else:
                    for i, item in enumerate(menu_warung):
                        print(f"{i+1}. {item[0]} - Rp{item[1]} ({item[2]})")
                input("Tekan Enter untuk kembali...")

            elif menu == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== Tambah Menu Baru ===")
                nama = input("Nama Menu: ")
                harga = input("Harga: ")
                kategori = input("Kategori (makanan/minuman): ").lower()
                if nama and harga.isdigit() and kategori in ['makanan', 'minuman']:
                    menu_warung.append([nama, int(harga), kategori])
                    print("Menu berhasil ditambahkan.")
                else:
                    print("Data tidak valid.")
                input("Tekan Enter untuk kembali...")

            elif menu == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== Ubah Menu ===")
                if len(menu_warung) == 0:
                    print("Belum ada menu.")
                else:
                    for i, item in enumerate(menu_warung):
                        print(f"{i+1}. {item[0]} - Rp{item[1]} ({item[2]})")
                    index = input("Nomor menu yang ingin diubah: ")
                    if index.isdigit():
                        idx = int(index) - 1
                        if 0 <= idx < len(menu_warung):
                            nama = input("Nama baru: ")
                            harga = input("Harga baru: ")
                            kategori = input("Kategori baru (makanan/minuman): ").lower()
                            if nama and harga.isdigit() and kategori in ['makanan', 'minuman']:
                                menu_warung[idx] = [nama, int(harga), kategori]
                                print("Menu berhasil diubah.")
                            else:
                                print("Data tidak valid.")
                        else:
                            print("Nomor menu tidak ditemukan.")
                    else:
                        print("Input harus angka.")
                input("Tekan Enter untuk kembali...")

            elif menu == '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== Hapus Menu ===")
                if len(menu_warung) == 0:
                    print("Belum ada menu.")
                else:
                    for i, item in enumerate(menu_warung):
                        print(f"{i+1}. {item[0]} - Rp{item[1]} ({item[2]})")
                    index = input("Nomor menu yang ingin dihapus: ")
                    if index.isdigit():
                        idx = int(index) - 1
                        if 0 <= idx < len(menu_warung):
                            del menu_warung[idx]
                            print("Menu berhasil dihapus.")
                        else:
                            print("Nomor menu tidak ditemukan.")
                    else:
                        print("Input harus angka.")
                input("Tekan Enter untuk kembali...")

            elif menu == '5':
                break
            else:
                print("Menu tidak valid.")
                input("Tekan Enter untuk lanjut...")

        # MENU USER
        while role == 'user':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== Menu Pengguna Warung Padang ===")
            print("1. Lihat Menu")
            print("2. Pesan Menu")
            print("3. Logout")
            menu = input("Pilih menu: ")

            if menu == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== Daftar Menu ===")
                if len(menu_warung) == 0:
                    print("Belum ada menu.")
                else:
                    for i, item in enumerate(menu_warung):
                        print(f"{i+1}. {item[0]} - Rp{item[1]} ({item[2]})")
                input("Tekan Enter untuk kembali...")

            elif menu == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== Pemesanan Menu ===")
                if len(menu_warung) == 0:
                    print("" \
                    "Belum ada menu untuk dipesan.")
                else:
                    if username not in pesanan:
                        pesanan[username] = []
                    while True:
                        for i, item in enumerate(menu_warung):
                            print(f"{i+1}. {item[0]} - Rp{item[1]} ({item[2]})")
                        pilih = input("Pilih nomor menu (atau '0' untuk selesai): ")
                        if pilih == '0':
                            break
                        if pilih.isdigit():
                            idx = int(pilih) - 1
                            if 0 <= idx < len(menu_warung):
                                jumlah = input("Jumlah: ")
                                if jumlah.isdigit():
                                    jumlah = int(jumlah)
                                    subtotal = menu_warung[idx][1] * jumlah
                                    pesanan[username].append([menu_warung[idx][0], jumlah, subtotal])
                                    print(f"✅ {menu_warung[idx][0]} x{jumlah} ditambahkan ke pesanan.")
                                else:
                                    print("Jumlah harus angka.")
                            else:
                                print("Nomor menu tidak valid.")
                        else:
                            print("Input harus angka.")
                    # Tampilkan ringkasan pesanan
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== Ringkasan Pesanan ===")
                    total = 0
                    for item in pesanan[username]:
                        print(f"- {item[0]} x{item[1]} = Rp{item[2]}")
                        total += item[2]
                    print(f"Total Bayar: Rp{total}")
                input("Tekan Enter untuk kembali...")

            elif menu == '3':
                break
            else:
                print("Menu tidak valid.")
                input("Tekan Enter untuk lanjut...")

    # REGISTER
    elif pilihan == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== Registrasi Pengguna Baru ===")
        username = input("Username: ")
        password = input("Password: ")
        role = 'user'
        sudah_ada = False
        for user in users:
            if user[0] == username:
                sudah_ada = True
                break
        if sudah_ada:
            print("Username sudah digunakan.")
        else:
            users.append([username, password, role])
            print("Registrasi berhasil!")
        input("Tekan Enter untuk lanjut...")

    # KELUAR
    elif pilihan == '3':
        print("👋 Keluar dari program.")
        break

    else:
        print("Menu tidak valid.")
        input("Tekan Enter untuk lanjut...")
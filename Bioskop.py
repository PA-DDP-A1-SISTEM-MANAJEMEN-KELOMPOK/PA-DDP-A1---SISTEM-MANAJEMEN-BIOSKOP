import json
from prettytable import PrettyTable
import pwinput
from datetime import datetime
import os
import time




'''================================================='''
'''                      JSON                       '''
'''================================================='''
def bacafilm():
    with open('PA DDP\Daftar Film.json', 'r') as file:
        return json.load(file)
    
def tulisfilm(data):
    with open("PA DDP\Daftar Film.json", "w")as file:
        json.dump(data, file, indent=4)

def bacacafe():
    with open('PA DDP\Daftar isi cafe.json', 'r') as file:
        return json.load(file)
    
def tuliscafe(data):
    with open("PA DDP\Daftar isi cafe.json", "w")as file:
        json.dump(data, file, indent=4)

def bacauser():
    with open('PA DDP\\akunpelanggan.json', 'r') as file:
        return json.load(file)
    
def tulisuser(data):
    with open("PA DDP\\akunpelanggan.json", "w")as file:
        json.dump(data, file, indent=4)

def bacapengajuan():
    with open("PA DDP\\Pengajuan.json", "r") as file:
        return json.load(file)

def tulispengajuan(data):
    with open("PA DDP\\Pengajuan.json", "w") as file:
        json.dump(data, file, indent=4)

def bacaklien():
    with open("PA DDP\\dataklien.json", "r") as file:
        return json.load(file)

def tulisklien(data):
    with open("PA DDP\\dataklien.json", "w") as file:
        json.dump(data, file, indent=4)

def simpanakun(akun_login):
    with open("PA DDP\\akunpelanggan.json", "r")as file:
        data= json.load(file)
    for akun in data["akun"]:
        if akun["username"] == akun_login["username"]:
            akun.update(akun_login)
    with open("PA DDP\\akunpelanggan.json", "w")as file:
        json.dump(data, file, indent=4)


'''================================================='''
#Username dan Password Staff
akun_staff = {
    "Gita":{ "password": "010", "role": "staffbioskop"},
    "Arza":{ "password": "007", "role": "staffbioskop"},
    "Fadil":{ "password": "032", "role": "staffcafe"}
}
'''================================================='''




'''================================================='''
'''                  MENU UTAMA                     '''
'''================================================='''
def MenuUtama():
    os.system("cls")
    try:
        while True:
            print("======== MENU UTAMA ========")
            print("1. Menu Staff")
            print("2. Menu Pelanggan")
            print("3. Menu Client")
            print("4. Keluar")
            print("===========================")
            pilihan = input("Pilih menu [1-4]: ")
            if pilihan == "1":
                lanjutanstaff()
            elif pilihan == "2":
                konfirmasipelanggan()
            elif pilihan == "3":
                konfirmasiclient()
            elif pilihan == "4":
                print("Terima kasih telah menggunakan program ini!")
                break
                
            else:
                print("Pilihan tidak tersedia")
                MenuUtama()
    except ValueError:
        print("Input harus berupa angka 1-4.")
        MenuUtama()




'''================================================='''
'''                  LOGIN STAFF                    '''
'''================================================='''
def loginstaff():
        os.system("cls")
        username = input("Masukkan Username Staff: ")
        password = (pwinput.pwinput("Masukkan Password Staff: "))
        if username in akun_staff and akun_staff[username]["password"] == password:
            print("Login Berhasil")
            return akun_staff[username]["role"]
        else:
            print("Username atau Password salah")
            MenuUtama()




'''================================================='''
'''              LANJUTAN LOGIN STAFF               '''
'''================================================='''
def lanjutanstaff():
        os.system("cls")
        role = loginstaff()
        if role == "staffbioskop":
            menustaffb()
        elif role == "staffcafe":
            menustaffc()
        else:
            print("Staff tidak terdata")
            MenuUtama()




'''================================================='''
'''              MENU STAFF BIOSKOP                 '''
'''================================================='''
def menustaffb():
    os.system("cls")
    while True:
        print("======== MENU STAFF BIOSKOP ========")
        print("1. Tambahkan Data Film")
        print("2. Menampilkan Daftar Film")
        print("3. Memperbarui Data Film")
        print("4. Menghapus Data Film")
        print("5. Mengecek status pengajuan")
        print("6. Kembali")
        print("===================================")
        staffb = int(input("Masukkan Pilihan Menu(1-5): "))
        if staffb == 1:
            menustaffb1()
        elif staffb == 2:
            menustaffb2()
        elif staffb == 3:
            menustaffb3()
        elif staffb == 4:
            menustaffb4()
        elif staffb == 5:
            menustaffb5()
        elif staffb == 6:
            MenuUtama()
        else:
            print("Pilihan tidak tersedia")
            continue

def menustaffb1():
    os.system("cls")
    data = bacafilm()
    Film = input("Masukkan judul film: ").capitalize()
    Jam = input("Masukkan jam tayang film (format HH.MM): ")
    Harga = int(input("Masukkan harga film(6-10 M koin): "))
    Ruang = int(input("Masukkan ruang theater film: "))
    def ke_menit(jam_str):
        jam_str = jam_str.replace(":", ".") 
        jam, menit = jam_str.split(".")
        return int(jam) * 60 + int(menit)
    jam_input = ke_menit(Jam)
    for paket in data["Daftar"]:
        jam_mulai = ke_menit(paket["Jam mulai"])
        jam_selesai = ke_menit(paket["Jam selesai"])
        if jam_mulai <= jam_input <= jam_selesai:
            paket["item"].append({
                "film": Film,
                "tayang": Jam,
                "mkoin": Harga,
                "theater": Ruang
            })
            print(f"Film {Film} berhasil ditambahkan ke {paket['paket film']}")
            tulisfilm(data)
            return
        if jam_mulai > jam_selesai:  
            if jam_input >= jam_mulai or jam_input <= jam_selesai:
                paket["item"].append({
                    "film": Film,
                    "tayang": Jam,
                    "mkoin": Harga,
                    "theater": Ruang
                })
                print(f"Film {Film} berhasil ditambahkan ke {paket['paket film']}")
                tulisfilm(data)
                return
    print("Jam tayang tidak sesuai dengan paket film manapun!")

def menustaffb2():
    os.system("cls")
    data = bacafilm()
    print("Daftar Paket Film:")
    for i, paket in enumerate(data["Daftar"]):
        print(f"{i+1}. {paket["paket film"]}")
    paket = int(input("Masukkan Paket Film Yang Ingin Ditampilkan(1-4): "))
    if paket > 0 and paket <= len(data["Daftar"]):
        paket_film = data["Daftar"][paket - 1]
        tabel = PrettyTable()
        tabel.title = f"Daftar Film {paket_film["paket film"]}"
        tabel.field_names =["Nama Film", "Jam Tayang", "Harga(M koin)", "Theater"]
        for item in paket_film["item"]:
            tabel.add_row([item["film"], item["tayang"], item["mkoin"], item["theater"]])
        print(f"Menampilkan {paket_film['paket film']}")
        print(tabel)

def menustaffb3():
    os.system("cls")
    data = bacafilm()
    print("Daftar Paket Film:")
    for i, paket in enumerate(data["Daftar"]):
        print(f"{i+1}. {paket["paket film"]} ({paket["Jam mulai"]} - {paket["Jam selesai"]})")
    try:
        pilihan_paket = int(input("Pilih paket film yang ingin diperbarui (nomor): "))
        if pilihan_paket < 1 or pilihan_paket > len(data["Daftar"]):
            print("Pilihan paket tidak valid.")
            return
        paket_film = data["Daftar"][pilihan_paket - 1]
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return
    if not paket_film["item"]:
        print(f"Tidak ada film dalam paket {paket_film['paket film']}.")
        return
    print(f"\nDaftar Film dalam {paket_film["paket film"]}:")
    tabel = PrettyTable()
    tabel.field_names =["Nama Film", "Jam Tayang", "Harga(M koin)", "Theater Film"]
    list_nama_film = []
    for item in paket_film["item"]:
        tabel.add_row([item["film"], item["tayang"], item["mkoin"], item["theater"]])
        list_nama_film.append(item["film"].capitalize())
    print(tabel)
    nama_film_dipilih = input("Masukkan Nama Film yang ingin diperbarui: ").capitalize().strip()
    film_yang_diubah = None
    for item in paket_film["item"]:
        if item["film"].capitalize() == nama_film_dipilih.capitalize():
            film_yang_diubah = item
            break
    if film_yang_diubah is None:
        print(f"Film dengan nama '{nama_film_dipilih}' tidak ditemukan dalam paket {paket_film['paket film']}.")
        return
    print(f"\nMemperbarui Film: {film_yang_diubah['film']}")
    new_tayang = input(f"Masukkan jam tayang baru (kosongkan jika tidak ingin diubah, saat ini: {film_yang_diubah['tayang']}): ")
    if new_tayang:
        try:
            jam_input = datetime.strptime(new_tayang, '%H:%M').time()
            jam_mulai_paket = datetime.strptime(paket_film["Jam mulai"], '%H:%M').time()
            jam_selesai_paket = datetime.strptime(paket_film["Jam selesai"], '%H:%M').time()
            if jam_mulai_paket <= jam_input < jam_selesai_paket:
                film_yang_diubah["tayang"] = new_tayang
            else:
                print(f"Jam tayang {new_tayang} tidak sesuai dengan rentang paket ({paket_film['Jam mulai']} - {paket_film['Jam selesai']}). Jam tayang tidak diubah.")
        except ValueError:
            print("Format jam tayang tidak valid (gunakan HH:MM). Jam tayang tidak diubah.")
    new_harga = input(f"Masukkan harga film baru dalam M Koin (kosongkan jika tidak ingin diubah, saat ini: {film_yang_diubah['mkoin']}): ")
    if new_harga:
        try:
            film_yang_diubah["mkoin"] = int(new_harga)
        except ValueError:
            print("Harga harus berupa angka. Harga tidak diubah.")
    new_ruang = input(f"Masukkan ruang tayang baru (kosongkan jika tidak ingin diubah, saat ini: {film_yang_diubah['theater']}): ")
    if new_ruang:
        film_yang_diubah["Ruang"] = new_ruang
    tulisfilm(data)
    print("\nData film berhasil diperbarui.")
    print("--- Data Film Setelah Diperbarui ---")
    print(f"--- Daftar Film {paket_film['paket film']} Setelah Diperbarui ---")
    updated_tabel = PrettyTable()
    updated_tabel.title = f"Daftar Film {paket_film["paket film"]}" 
    updated_tabel.field_names =["Nama Film", "Jam Tayang", "Harga(M koin)", "Ruangan Film"]
    for item in paket_film["item"]:
        updated_tabel.add_row([item["film"], item["tayang"], item["mkoin"], item["theater"]])
    print(updated_tabel)

def menustaffb4():
    os.system("cls")
    data = bacafilm()
    menustaffb2()
    paket = int(input("Masukkan Paket Film Yang Ingin Dihapus(1-4): "))
    if paket > 0 and paket <= len(data["Daftar"]):
        paket_film = data["Daftar"][paket - 1]
        nama_film = input("Masukkan Nama Film yang Ingin Dihapus: ").capitalize().strip()
        film_dihapus = None
        for item in paket_film["item"]:
            if item["film"] == nama_film:
                film_dihapus = item
                break
        if film_dihapus:
            paket_film["item"].remove(film_dihapus)
            tulisfilm(data)
            print(f"Film '{film_dihapus['film']}' berhasil dihapus dari paket {paket_film['paket film']}.")
        else:
            print(f"Film dengan nama '{nama_film}' tidak ditemukan dalam paket {paket_film['paket film']}.")

def menustaffb5():
    os.system("cls")
    data_klien = bacaklien()
    daftar_produser = []
    for akun in data_klien["klien"]:
        if "pengajuan" in akun and len(akun["pengajuan"]) > 0:
            daftar_produser.append(akun)
    if not daftar_produser:
        print("Belum ada pengajuan dari client.")
        return
    print("======== DAFTAR PRODUSER DENGAN PENGAJUAN ========")
    for i, akun in enumerate(daftar_produser, start=1):
        print(f"{i}. {akun['produser']}")
    print("===================================================")
    pilih_produser = input("Masukkan nomor produser yang ingin dilihat (0 untuk kembali): ")
    if not pilih_produser.isdigit():
        print("Input tidak valid.")
        return
    pilih_produser = int(pilih_produser)
    if pilih_produser == 0:
        return
    if pilih_produser < 1 or pilih_produser > len(daftar_produser):
        print("Nomor produser tidak valid.")
        return
    produser = daftar_produser[pilih_produser - 1]
    pengajuan_film = [p for p in produser["pengajuan"] if "judul film" in p]
    if not pengajuan_film:
        print("Tidak ada pengajuan film dari produser ini.")
        return
    print(f"======== DAFTAR PENGAJUAN FILM {produser['produser']} ========")
    for i, film in enumerate(pengajuan_film, start=1):
        jenis = film.get("jenis", "tayang")
        print(f"{i}. {film['judul film']} | Jenis: {jenis} | Status: {film.get('status', 'menunggu')}")
    print("===============================================================")
    pilih_film = input("Masukkan nomor film yang ingin diproses (0 untuk kembali): ")
    if not pilih_film.isdigit():
        print("Input tidak valid.")
        return
    pilih_film = int(pilih_film)
    if pilih_film == 0:
        return
    if pilih_film < 1 or pilih_film > len(pengajuan_film):
        print("Nomor film tidak valid.")
        return
    film = pengajuan_film[pilih_film - 1]
    jenis = film.get("jenis", "tayang")
    print(f"Film: {film['judul film']} | Pengajuan: {jenis}")
    keputusan = input("Apakah pengajuan ini disetujui? (y/n): ").lower()
    if keputusan == "y":
        if jenis == "tayang":
            print("Pengajuan tayang disetujui. Tambahkan film ke daftar bioskop.")
            input("Tekan Enter untuk melanjutkan...")
            menustaffb1()
        elif jenis == "tarik":
            print("Pengajuan penarikan disetujui. Hapus film dari daftar bioskop.")
            input("Tekan Enter untuk melanjutkan...")
            menustaffb4()
    elif keputusan == "n":
        print("Pengajuan ditolak. Kembali ke menu staff bioskop.")
        input("Tekan Enter untuk melanjutkan...")
        menustaffb()
    else:
        print("Pilihan tidak valid.")




def menustaffc():
    os.system("cls")
    while True:
        print("\n======== MENU STAFF CAFE ========")
        print("1. Tambah Menu Cafe")
        print("2. Lihat Menu Cafe")
        print("3. Tambah Merchandise")
        print("4. Lihat Merchandise")
        print("5. Hapus Merchandise")
        print("6. Kembali")
        print("=================================")
        pilih = input("Pilih menu [1-6]: ")
        if pilih == "1":
            menustaffc1()
        elif pilih == "2":
            menustaffc2()
        elif pilih == "3":
            menustaffc3()
        elif pilih == "4":
            menustaffc4()
        elif pilih == "5":
            menustaffc5()
        elif pilih == "6":
            break
        else:
            print("Pilihan tidak tersedia!")


def menustaffc1():
    os.system("cls")
    data = bacacafe()
    paket = input("Masukkan nama paket menu: ")
    makanan = input("Masukkan nama makanan: ")
    minuman = input("Masukkan nama minuman: ")
    while True:
        try:
            mkoin = int(input("Masukkan harga mkoin (8 - 15): "))
            if 8 <= mkoin <= 15:
                break
            else:
                print(" Range harga mkoin untuk menu cafe yaitu 8 sampai 15!")
        except ValueError:
            print("Input harus berupa angka!")
    if "Kategori" not in data:
        data["Kategori"] = []
    kategori_cafe = None
    for k in data["Kategori"]:
        if k["kategori"].lower() == "menu cafe":
            kategori_cafe = k
            break
    if not kategori_cafe:
        kategori_cafe = {"kategori": "menu cafe", "item": []}
        data["Kategori"].append(kategori_cafe)
    kategori_cafe["item"].append({
        "paket": paket,
        "nama makanan": makanan,
        "nama minuman": minuman,
        "mkoin": mkoin
    })
    tuliscafe(data)
    print("Menu cafe berhasil ditambahkan!")
    input("Tekan Enter untuk melanjutkan...")
    menustaffc()


def menustaffc2():
    os.system("cls")
    data = bacacafe()
    menu_cafe = None
    for kategori in data["Kategori"]:
        if kategori["kategori"].lower() == "menu cafe":
            menu_cafe = kategori["item"]
            break
    if not menu_cafe:
        print("Tidak ada data menu cafe.")
        menustaffc()
        return
    tabel = PrettyTable()
    tabel.title = "Daftar Menu Cafe XXI"
    tabel.field_names = ["No", "Paket", "Makanan", "Minuman", "Harga (M Koin)"]
    for i, item in enumerate(menu_cafe, start=1):
        tabel.add_row([i, item["paket"], item["nama makanan"], item["nama minuman"], item["mkoin"]])
    print(tabel)
    input("Tekan Enter untuk melanjutkan...")
    menustaffc()


def menustaffc3():
    os.system("cls")
    data = bacacafe()
    nama = input("Masukkan nama merchandise: ")
    while True:
        try:
            stock = int(input("Masukkan stock merchandise (1 - 100): "))
            if 1 <= stock <= 100:
                break
            else:
                print("Stok merchandise hanya 1 sampai 100!")
        except ValueError:
            print("Input harus berupa angka!")
    while True:
        try:
            harga = int(input("Masukkan harga merchandise (60000 - 2000000): "))
            if 60000 <= harga <= 2000000:
                break
            else:
                print("Range harga merchandise yaitu 60000 sampai 2000000!")
        except ValueError:
            print("Input harus berupa angka!")
    if "Kategori" not in data:
        data["Kategori"] = []
    kategori_merch = None
    for k in data["Kategori"]:
        if k["kategori"].lower() == "merch":
            kategori_merch = k
            break
    if not kategori_merch:
        kategori_merch = {"kategori": "merch", "item": []}
        data["Kategori"].append(kategori_merch)
    no_baru = len(kategori_merch["item"]) + 1
    kategori_merch["item"].append({
        "no": no_baru,
        "nama": nama,
        "stock": stock,
        "harga": harga
    })
    tuliscafe(data)
    print("Merchandise berhasil ditambahkan!")
    input("Tekan Enter untuk melanjutkan...")
    menustaffc()


def menustaffc4():
    os.system("cls")
    merch = None
    data = bacacafe()
    for kategori in data["Kategori"]:
        if kategori["kategori"].lower() == "merch":
            merch = kategori["item"]
            break
    if not merch:
        print("Tidak ada data merchandise.")
        menustaffc()
        return
    tabel = PrettyTable()
    tabel.title = "Daftar Merchandise Cafe XXI"
    tabel.field_names = ["No", "Nama", "Stok", "Harga (Rp)"]
    for item in merch:
        tabel.add_row([item["no"], item["nama"], item["stock"], item["harga"]])
    print(tabel)
    input("Tekan Enter untuk melanjutkan...")
    menustaffc()


def menustaffc5():
    os.system("cls")
    data = bacacafe()
    merch = None
    for kategori in data["Kategori"]:
        if kategori["kategori"].lower() == "merch":
            merch = kategori["item"]
            break
    if merch is None or not merch:
        print("Tidak ada merchandise untuk dihapus.")
        menustaffc()
        return
    tabel = PrettyTable()
    tabel.title = "Daftar Merchandise Cafe XXI"
    tabel.field_names = ["No", "Nama", "Stok", "Harga (Rp)"]
    for item in merch:
        tabel.add_row([item["no"], item["nama"], item["stock"], item["harga"]])
    print(tabel)
    nama = input("Masukkan nama merchandise yang ingin dihapus: ").capitalize()
    for item in merch:
        if item["nama"] == nama:
            merch.remove(item)
            tuliscafe(data)
            print("Merchandise berhasil dihapus.")
            input("Tekan Enter untuk melanjutkan...")
            menustaffc()
            return
    print("Merchandise tidak ditemukan.")
    input("Tekan Enter untuk melanjutkan...")
    menustaffc()

'''================================================='''
'''                    MENU USER                    '''
'''================================================='''
def menupelanggan():

    statususer()
    print("======== DAFTAR MENU PENGGUNA ========")
    print("1. Melihat Daftar Film")
    print("2. Membeli Tiket Film")
    print("3. Menu Cafe")
    print("4. Top Up Mkoin")
    print("5. Top Up Saldo")
    print("6. Kembali")
    print("===================================")
    pelanggan = input("Masukkan Pilihan Menu(1-6): ")
    if pelanggan == "1":
        menupelanggan1()
    elif pelanggan == "2":
        menupelanggan2()
    elif pelanggan == "3":
        menucafep()
    elif pelanggan == "4":
        menupelanggan4()
    elif pelanggan == "5":
        menupelanggan5()
    elif pelanggan == "6":
        MenuUtama()
    else:
        print("Pilihan tidak tersedia")


def menupelanggan1():
    os.system("cls")
    data = bacafilm()
    waktu_perangkat = datetime.now().time()
    tampil = False
    for Daftar in data["Daftar"]:
        mulai = datetime.strptime(Daftar["Jam mulai"], "%H:%M").time()
        selesai = datetime.strptime(Daftar["Jam selesai"], "%H:%M").time()
        if mulai <= selesai:
            if mulai <= waktu_perangkat <= selesai:
                tampil = True
        else:
            if waktu_perangkat >= mulai or waktu_perangkat <= selesai:
                tampil = True
        if tampil:
            tabel = PrettyTable()
            tabel.title = f"Daftar Film ({Daftar['paket film']})"
            tabel.field_names = ["Nama Film", "Jam Tayang", "Harga(M koin)", "Theater"]
            for item in Daftar["item"]:
                tabel.add_row([item["film"], item["tayang"], item["mkoin"], item["theater"]])
            print(f"Menampilkan {Daftar['paket film']}")
            print(tabel, flush=True)
            input("Tekan Enter untuk melanjutkan...")
            menupelanggan()
            return
    print("Tidak ada film yang tayang pada jam ini.")
    input("Tekan Enter untuk kembali...")
    menupelanggan()

def menupelanggan2():
    os.system("cls")
    try:
        data = bacafilm()
        global akun_login
        waktu_perangkat = datetime.now().time()
        paket_aktif = None
        for Daftar in data["Daftar"]:
            mulai = datetime.strptime(Daftar["Jam mulai"], "%H:%M").time()
            selesai = datetime.strptime(Daftar["Jam selesai"], "%H:%M").time()
            if mulai <= selesai:
                if mulai <= waktu_perangkat <= selesai:
                    paket_aktif = Daftar
            else:
                if waktu_perangkat >= mulai or waktu_perangkat <= selesai:
                    paket_aktif = Daftar
        if not paket_aktif:
            print("Tidak ada film yang tayang saat ini.")
            input("Tekan Enter untuk kembali...")
            menupelanggan()
            return
        tabel = PrettyTable()
        tabel.title = f"Daftar Film ({paket_aktif['paket film']})"
        tabel.field_names = ["No", "Nama Film", "Jam Tayang", "Harga(M koin)", "Theater", "Kursi Tersisa"]
        for i, item in enumerate(paket_aktif["item"], start=1):
            if "kursi" not in item:
                item["kursi"] = 20
            tabel.add_row([i, item["film"], item["tayang"], item["mkoin"], item["theater"], item["kursi"]])
        print(tabel)
        try:
            pilih = int(input("Masukkan nomor film yang ingin dibeli: "))
        except ValueError:
            print("Input harus berupa angka.")
            input("Tekan Enter untuk kembali...")
            menupelanggan()
            return
        if pilih < 1 or pilih > len(paket_aktif["item"]):
            print("Nomor film tidak valid.")
            input("Tekan Enter untuk kembali...")
            menupelanggan()
            return
        film_dipilih = paket_aktif["item"][pilih - 1]
        if film_dipilih["kursi"] <= 0:
            print("Maaf, semua kursi untuk film ini sudah habis.")
            input("Tekan Enter untuk kembali...")
            menupelanggan()
            return
        if akun_login["mkoin"] < film_dipilih["mkoin"]:
            print("M Koin Anda tidak cukup untuk membeli tiket ini.")
            input("Tekan Enter untuk kembali...")
            menupelanggan()
            return
        akun_login["mkoin"] -= film_dipilih["mkoin"]
        film_dipilih["kursi"] -= 1
        simpanakun(akun_login)
        tulisfilm(data)
        print("="*40)
        print("           INVOICE - XXI")
        print(f"Atas nama : {akun_login['username']}")
        print(f"Film      : {film_dipilih['film']}")
        print(f"Jam       : {film_dipilih['tayang']}")
        print(f"Theater   : {film_dipilih['theater']}")
        print(f"Harga     : {film_dipilih['mkoin']} M Koin")
        print("="*40)
        input("Tekan Enter untuk melanjutkan...")
        statususer()
        menupelanggan()
    except Exception as e:
        print("Terjadi kesalahan:", e)
        input("Tekan Enter untuk kembali...")
        menupelanggan()



def menupelanggan4():
    os.system("cls")
    try:
        data = bacauser()
        for akun in data["akun"]:
            if akun["username"] == akun_login["username"]:
                print(f"M Koin saat ini: {akun['mkoin']}")
                jumlah = int(input("Masukkan jumlah M Koin yang ingin dibeli (min 5, maks 500): "))
                if jumlah < 5 or jumlah > 500:
                    print("Jumlah top up M Koin tidak valid")
                    return
                harga = jumlah * 5000
                if akun["saldo"] < harga:
                    print("Saldo tidak cukup")
                    return
                akun["saldo"] -= harga
                akun["mkoin"] += jumlah
                akun_login["saldo"] = akun["saldo"]
                akun_login["mkoin"] = akun["mkoin"]
                tulisuser(data)
                print(f"Top up M Koin berhasil. Saldo tersisa: {akun['saldo']}, total M Koin: {akun['mkoin']}")
                input("Tekan Enter untuk melanjutkan...")
                return
        print("Akun tidak ditemukan")
        input("Tekan Enter untuk melanjutkan...")
    except ValueError:
        print("Input harus berupa angka.")
        menupelanggan()

def menupelanggan5():
    os.system("cls")
    try:
        data = bacauser()
        for akun in data["akun"]:
            if akun["username"] == akun_login["username"]:
                print(f"Saldo saat ini: {akun['saldo']}")
                jumlah = int(input("Masukkan jumlah top up (min 50000, maks 2000000): "))
                if jumlah < 50000 or jumlah > 2000000:
                    print("Jumlah top up tidak valid")
                    return
                akun["saldo"] += jumlah
                akun_login["saldo"] = akun["saldo"]
                tulisuser(data)
                print(f"Top up berhasil. Saldo baru: {akun['saldo']}")
                input("Tekan Enter untuk melanjutkan...")
                return
        print("Akun tidak ditemukan")
        input("Tekan Enter untuk melanjutkan...")
    except ValueError:
        print("Input harus berupa angka.")
        menupelanggan()


def menucafep():
    data = bacacafe()
    print("======== MENU CAFE PELANGGAN ========")
    print("1. Membeli Paket Cafe (M Koin)")
    print("2. Membeli Merchandise (Saldo)")
    print("3. Kembali")
    print("=====================================")
    pilih = input("Masukkan pilihan (1-3): ")
    if pilih == "1":
        menubeli_paketcafe(data)
    elif pilih == "2":
        menubeli_merch(data)
    elif pilih == "3":
        menupelanggan()
    else:
        print("Pilihan tidak tersedia.")
        menucafep()

def menubeli_paketcafe(data):
    os.system("cls")
    global akun_login
    data = bacacafe()
    menu_cafe = None
    for kategori in data["Kategori"]:
        if kategori["kategori"].lower() == "menu cafe":
            menu_cafe = kategori["item"]
            break
    if not menu_cafe:
        print("Tidak ada data menu cafe.")
        input("Tekan Enter untuk kembali...")
        menucafep()
        return
    tabel = PrettyTable()
    tabel.title = "Daftar Paket Cafe XXI"
    tabel.field_names = ["No", "Paket", "Makanan", "Minuman", "Harga (M Koin)"]
    for i, item in enumerate(menu_cafe, start=1):
        tabel.add_row([i, item["paket"], item["nama makanan"], item["nama minuman"], item["mkoin"]])
    print(tabel)
    try:
        pilih = int(input("Masukkan nomor paket yang ingin dibeli: "))
    except ValueError:
        print("Input harus berupa angka.")
        input("Tekan Enter untuk kembali...")
        menucafep()
        return
    if pilih < 1 or pilih > len(menu_cafe):
        print("Nomor paket tidak ditemukan.")
        input("Tekan Enter untuk kembali...")
        menucafep()
        return
    paket_dipilih = menu_cafe[pilih - 1]
    harga = paket_dipilih["mkoin"]
    if akun_login["mkoin"] < harga:
        print("M Koin Anda tidak cukup untuk membeli paket ini.")
        input("Tekan Enter untuk kembali...")
        menucafep()
        return
    akun_login["mkoin"] -= harga
    simpanakun(akun_login)
    print("="*40)
    print("     STRUK PEMBELIAN - CAFE XXI")
    print(f"Atas nama : {akun_login['username']}")
    print(f"Paket     : {paket_dipilih['paket']}")
    print(f"Makanan   : {paket_dipilih['nama makanan']}")
    print(f"Minuman   : {paket_dipilih['nama minuman']}")
    print(f"Harga     : {harga} M Koin")
    print(f"Sisa M Koin: {akun_login['mkoin']}")
    print("="*40)
    input("Tekan Enter untuk melanjutkan...")
    statususer()
    menucafep()

def menubeli_merch(data):
    os.system("cls")
    global akun_login
    data = bacacafe()
    merch = None
    for kategori in data["Kategori"]:
        if kategori["kategori"].lower() == "merch":
            merch = kategori["item"]
            break
    if not merch:
        print("Tidak ada data merchandise.")
        input("Tekan Enter untuk kembali...")
        menucafep()
        return
    tabel = PrettyTable()
    tabel.title = "Daftar Merchandise Cafe XXI"
    tabel.field_names = ["No", "Nama", "Stok", "Harga (Rp)"]
    for item in merch:
        tabel.add_row([item["no"], item["nama"], item["stock"], item["harga"]])
    print(tabel)
    try:
        pilih = int(input("Masukkan nomor merchandise yang ingin dibeli: "))
    except ValueError:
        print("Input harus berupa angka.")
        input("Tekan Enter untuk kembali...")
        menucafep()
        return
    item_dipilih = next((item for item in merch if item["no"] == pilih), None)
    if not item_dipilih:
        print("Nomor merchandise tidak ditemukan.")
        input("Tekan Enter untuk kembali...")
        menucafep()
        return
    harga = item_dipilih["harga"]
    stok = int(item_dipilih["stock"])
    if stok <= 0:
        print("Stok merchandise ini sudah habis.")
        input("Tekan Enter untuk kembali...")
        menucafep()
        return
    if akun_login["saldo"] < harga:
        print("Saldo Anda tidak cukup untuk membeli merchandise ini.")
        input("Tekan Enter untuk kembali...")
        menucafep()
        return
    akun_login["saldo"] -= harga
    item_dipilih["stock"] = str(stok - 1)
    tuliscafe(data)
    simpanakun(akun_login)
    print("="*40)
    print("     STRUK PEMBELIAN - MERCH XXI")
    print(f"Atas nama : {akun_login['username']}")
    print(f"Merch     : {item_dipilih['nama']}")
    print(f"Harga     : Rp{harga}")
    print(f"Sisa saldo: Rp{akun_login['saldo']}")
    print("="*40)
    input("Tekan Enter untuk melanjutkan...")
    statususer()
    menucafep()





'''=========================================================================================================================='''
'''                                                                LOGIN USER                                                '''
'''=========================================================================================================================='''
def loginpelanggan():
    os.system("cls")
    try:
        global akun_login
        data = bacauser()
        kesempatan = 5
        while kesempatan > 0:
            username = input("Masukkan Username Anda: ").lower()
            password = pwinput.pwinput("Masukkan Password Anda: ")
            for akun in data["akun"]:
                if akun["username"] == username and akun["password"] == password:
                    print("Login Berhasil")
                    akun_login = akun.copy()
                    menupelanggan()
                    return
            kesempatan -= 1
            print(f"Username atau Password salah, sisa kesempatan login: {kesempatan}")
            if kesempatan == 0:
                print("Kesempatan login telah habis.")
                MenuUtama()
                return
    except FileNotFoundError:
        print("File akun tidak ditemukan.")
        MenuUtama()






'''================================================='''
'''                    REGIS USER                   '''
'''================================================'''
def buatakunpelanggan():
    os.system("cls")
    data = bacauser()
    print("======== BUAT AKUN PELANGGAN ========")
    username = input("Masukkan Username Baru (terdiri dari minimal 5 huruf): ").lower()
    if len(username) < 5 or not username.isalpha():
        print("Username harus terdiri dari minimal 5 huruf. Silakan coba lagi.")
        buatakunpelanggan()
    elif username in data:
        print("Username sudah terdaftar. Silakan coba lagi.")
        buatakunpelanggan()
    password = input("Masukkan Password Baru (terdiri dari 5 karakter gabungan huruf dan angka): ").lower()
    if len(password) < 5 or password.isalpha() or password.isdigit():
        print("Password harus terdiri dari minimal 5 karakter dan merupakan gabungan huruf dan angka. Silakan coba lagi.")
        buatakunpelanggan()
    data["akun"].append({
        "username": username,
        "password": password,
        "saldo": 0,
        "mkoin": 0
    })
    tulisuser(data)
    print("Akun berhasil dibuat!")
    loginpelanggan()




'''================================================='''
'''                    AKUN USER                    '''
'''================================================='''
def konfirmasipelanggan():
    os.system("cls")
    print("Apakah anda sudah memiliki akun? (y/n)")
    pilihan = input(": ").lower()
    if pilihan == "y":
        loginpelanggan()
    elif pilihan == "n":
        buatakunpelanggan()
    else:
        print("Pilihan tidak valid.")
        konfirmasipelanggan()

def statususer():
    os.system("cls")
    global akun_login
    print("======== STATUS AKUN ANDA ========")
    print(f"Username : {akun_login['username']}")
    print(f"M koin : {akun_login['mkoin']}")
    print(f"Saldo : {akun_login['saldo']}")
    print("===================================")


'''================================================='''
'''                    AKUN CLIENT                  '''
'''================================================='''
def konfirmasiclient():
    os.system("cls")
    print("Apakah anda sudah memiliki akun? (y/n)")
    pilihan = input(": ").lower()
    if pilihan == "y":
        loginclient()
    elif pilihan == "n":
        buatakunclient()
    else:
        print("Pilihan tidak valid.")
        konfirmasiclient()

def buatakunclient():
    os.system("cls")
    data = bacaklien()
    print("======== BUAT AKUN CLIENT ========")
    produser = input("Masukkan Nama Produser: ").capitalize()
    password = input("Masukkan Password Baru (minimal 5 karakter): ")
    if len(password) < 5:
        print("Password harus terdiri dari minimal 5 karakter.")
        MenuUtama()
        return
    data["klien"].append({
        "produser": produser,
        "password": password,
        "pengajuan": [
            {"tayang": ""},
            {"tarik": ""}
        ]
    })
    tulisklien(data)
    print("Akun client berhasil dibuat.")
    loginclient()

def loginclient():
    os.system("cls")
    try:
        global klien_login
        data = bacaklien()
        username = input("Masukkan nama produser: ")
        password = pwinput.pwinput("Masukkan password: ")
        for akun in data["klien"]:
            if akun["produser"] == username and akun["password"] == password:
                print("Login berhasil")
                klien_login = akun
                menuclient()
                return
        print("Login gagal, periksa kembali username atau password.")
        MenuUtama()
    except FileNotFoundError:
        print("File akun tidak ditemukan.")
        MenuUtama()




'''================================================='''
'''                    MENU CLIENT                  '''
'''================================================='''
def menuclient():
    os.system("cls")
    print("======== MENU CLIENT ========")
    print("1. Ajukan Penayangan Film")
    print("2. Ajukan Penarikan Film")
    print("3. Lihat Status Pengajuan")
    print("4. Kembali")
    print("================================")
    pilih = input("Pilih menu [1-4]: ")
    if pilih == "1":
        pengajuantayang()
    elif pilih == "2":
        pengajuantarik()
    elif pilih == "3":
        statuspengajuan()
    elif pilih == "4":
        MenuUtama()
    else:
        print("Pilihan tidak tersedia")
        menuclient()

def pengajuantayang():
    os.system("cls")
    data = bacapengajuan()
    judul = input("Masukkan judul film: ").capitalize()
    tayang = input("Masukkan waktu tayang yang diinginkan: ")
    data["pengajuan"].append({
        "produser": klien_login["produser"],
        "judul film": judul,
        "tayang": tayang,
        "status": "menunggu"
    })
    tulispengajuan(data)
    print("Pengajuan tayang berhasil dikirim.")
    input("Tekan Enter untuk melanjutkan...")
    menuclient()

def pengajuantarik():
    os.system("cls")
    data = bacaklien()
    for akun in data["klien"]:
        if akun["produser"] == klien_login["produser"]:
            judul = input("Masukkan judul film yang ingin ditarik: ").capitalize()
            alasan = input("Masukkan alasan penarikan: ")
            akun["pengajuan"].append({
                "judul film": judul,
                "alasan": alasan,
                "jenis": "tarik",
                "status": "menunggu"
            })
            tulisklien(data)
            print("Pengajuan penarikan berhasil dikirim.")
            input("Tekan Enter untuk melanjutkan...")
            menuclient()
            return

def statuspengajuan():
    os.system("cls")
    data = bacaklien()
    for akun in data["klien"]:
        if akun["produser"] == klien_login["produser"]:
            tabel = PrettyTable()
            tabel.title = "Status Pengajuan Film"
            tabel.field_names =["Judul Film", "Jenis", "Status"]
            for item in akun["pengajuan"]:
                tabel.add_row([item["judul film"], item["jenis"], item["status"]])
            print(tabel)
            input("Tekan Enter untuk melanjutkan...")
            menuclient()
            return

MenuUtama()
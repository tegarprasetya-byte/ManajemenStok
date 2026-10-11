# Mengimpor fungsi validasi untuk memeriksa input pengguna.
from stok.validasi import (
    validasi_kode_produk,
    validasi_harga,
    validasi_stok
)
# Mengimpor fungsi untuk menyimpan, membaca, dan memperbarui file produk.
from stok.fileio import (
    simpan_stok,
    baca_stok,
    tulis_ulang_stok
)
# Mengimpor fungsi untuk mencari produk dan mengolah data stok.
from stok.processing import(
    cari_produk,
    hitung_nilai_stok,
    buat_ringkasan
)
# Mengimpor class untuk merepresentasikan dan mengelola produk.
from stok.model import Produk, ManajemenStok

# Meminta data produk, memvalidasi input, lalu menyimpannya ke file.
def tambah_produk():
    #function yang digunakan untuk menambahkan Produk Baru
    try:
        kode_produk = validasi_kode_produk(input("Masukan Kode Produk :"))
        nama_produk = input("Masukan Nama Produk :")
        harga = validasi_harga(float(input("Masukan Harga Produk :")))
        jumlah_stok = validasi_stok(input("Masukan Jumlah Stok :"))
         # Menggabungkan data produk ke dalam dictionary.
        data_produk ={
            "kode_produk" : kode_produk,
            "nama_produk" : nama_produk,
            "harga_produk": harga,
            "stok_produk" : jumlah_stok
        }
        # Menyimpan data produk ke file.
        simpan_stok(data_produk)
        print("Produk Berhasil disimpan!")

    except (ValueError, TypeError) as error:
        print("Gagal menambahkan transaksi:", error)

# Membaca dan menampilkan seluruh produk yang tersimpan.
def tampilkan_produk():
    #Function yang digunakan untuk Menampilkan Daftar Produk
    daftar_produk = baca_stok()
    if not daftar_produk:
        print("Belum ada produk")
        return
    print("\n=== Daftar Produk ===")
    for nomor,produk in enumerate(daftar_produk,start=1):
        print(f"\nProduk ke-{nomor}")
        print("Kode :", produk['kode_produk'])
        print("Nama :", produk['nama_produk'])
        print("Harga:",produk['harga_produk'])
        print("Stok :", produk['stok_produk'])

# Mencari produk berdasarkan kode yang dimasukkan pengguna.
def cari_produk_menu():
    #Digunakan untuk Mencari Produk berdasarkan kode produk
    kode = input("Masukkan kode produk yang dicari: ").strip()
    produk = cari_produk(baca_stok(), kode)

    if produk is None:
        print("Produk tidak ditemukan.")
        return

    print("\n=== DETAIL PRODUK ===")
    print("Kode  :", produk["kode_produk"])
    print("Nama  :", produk["nama_produk"])
    print("Harga :",produk["harga_produk"])
    print("Stok  :", produk["stok_produk"])

def tambah_stok():
    #digunakan untuk memperbarui stok produk
    try:
        daftar_produk = baca_stok()

        kode = validasi_kode_produk(
            input("Masukkan kode produk: ")
        )

        produk = cari_produk(daftar_produk, kode)

        if produk is None:
            raise ValueError("Produk tidak ditemukan")

        jumlah = validasi_stok(
            input("Jumlah stok yang ditambahkan: ")
        )

        if jumlah == 0:
            raise ValueError("Jumlah penambahan harus lebih dari nol")

        produk["stok_produk"] += jumlah

        tulis_ulang_stok(daftar_produk)

        print("Stok berhasil ditambahkan.")
        print("Stok sekarang:", produk["stok_produk"])

    except (ValueError, TypeError) as error:
        print("Gagal menambahkan stok:", error)
    
    
def tampilkan_ringkasan():
    # Membaca data produk dari file.
    daftar_produk = baca_stok()

    # Mengubah dictionary menjadi objek Produk.
    daftar_objek = [
        Produk(
            produk["kode_produk"],
            produk["nama_produk"],
            produk["harga_produk"],
            produk["stok_produk"]
        )
        for produk in daftar_produk
    ]

    # Mengelola kumpulan objek produk.
    manajemen = ManajemenStok(daftar_objek)

    # Membuat ringkasan menggunakan keyword arguments.
    ringkasan = buat_ringkasan(
        jumlah_produk=len(daftar_objek),
        total_stok=sum(
            produk.stok_produk for produk in daftar_objek
        ),
        nilai_stok=manajemen.hitung_total_nilai_stok()
    )

    # Memastikan total nilai stok tidak negatif.
    assert ringkasan["nilai_stok"] >= 0, (
        "Nilai stok tidak boleh negatif"
    )

    print("\n=== RINGKASAN STOK ===")
    print("Jumlah jenis produk :", ringkasan["jumlah_produk"])
    print("Total seluruh stok  :", ringkasan["total_stok"])
    print("Nilai seluruh stok  : Rp", ringkasan["nilai_stok"])




def laporan_stok(): # membuat Laporan Produk dan Dimasukan ke file laporan/laporan.txt
    daftar_produk = baca_stok()

    if not daftar_produk:
        print("Belum ada data produk.")
        return

    try:
        with open("laporan/laporan_stok.txt", "w", encoding="utf-8") as file:
            file.write("========== LAPORAN STOK PRODUK ==========\n\n")

            total_nilai = 0

            for nomor, produk in enumerate(daftar_produk, start=1):
                harga = float(produk["harga_produk"])
                stok = int(produk["stok_produk"])
                nilai = harga * stok
                total_nilai += nilai

                file.write(f"Produk ke-{nomor}\n")
                file.write(f"Kode       : {produk['kode_produk']}\n")
                file.write(f"Nama       : {produk['nama_produk']}\n")
                file.write(f"Harga      : Rp{harga:,.0f}\n")
                file.write(f"Stok       : {stok}\n")
                file.write(f"Nilai Stok : Rp{nilai:,.0f}\n")
                file.write("-" * 40 + "\n")

            file.write(f"\nTotal jenis produk: {len(daftar_produk)}\n")
            file.write(f"Total nilai stok: Rp{total_nilai:,.0f}\n")

        print("Laporan stok berhasil disimpan ke laporan/laporan_stok.txt")

    except (ValueError, TypeError) as error:
        print("Gagal membuat laporan:", error)

def urutkan_produk(): # mengurutkan harga produk
    daftar_produk = baca_stok()

    if not daftar_produk:
        print("Belum ada produk")
        return

    daftar_produk.sort(
        key=lambda produk: produk["harga_produk"]
    )

    print("\n=== Produk Berdasarkan Harga ===")

    for produk in daftar_produk:
        print(
            produk["kode_produk"],
            produk["nama_produk"],
            produk["harga_produk"]
        )

def main(): #menu utama
    while True:
        print("\n==== Program Manajemen Stok ====")
        print("Fitur Utama...")
        print("1. Tambah Produk")
        print("2. Lihat Semua Produk")
        print("3. Cari Produk")
        print("4. Tambah Stok Produk")
        print("5. Ringkasan Stok")
        print("6. Buat Laporan Stok")
        print("7. Urutkan Produk Berdasarkan Harga")
        print("8. Keluar")
        pilihan = input("Masukan Piliihan :")
        if pilihan == "1":
            tambah_produk()
        elif pilihan == "2":
            tampilkan_produk()
        elif pilihan =="3":
            cari_produk_menu()
        elif pilihan =="4":
            tambah_stok()
        elif pilihan =="5":
            tampilkan_ringkasan()
        elif pilihan == "6":
            laporan_stok()
        elif pilihan == "7":
            urutkan_produk()
        elif pilihan == "8":
            print("Keluar Dari Program")
            break
        else:
            print("Pilihan tidak Valid")

if __name__ == "__main__":
    main()
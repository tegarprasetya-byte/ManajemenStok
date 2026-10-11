def simpan_stok(data_produk): # Membuat file produk jika belum ada, lalu menambahkan data produk.
    #menyimpan stok ke file data/produk.txt
    try:
        with open("data/produk.txt","x", encoding="utf-8"): # Mode x digunakan untuk membuat file baru tanpa menimpa file lama.
            pass
    except FileExistsError:
        pass

    with open("data/produk.txt", "a", encoding="utf-8") as file: # Menambahkan Data Baru di akhir
        file.write(
            f"{data_produk['kode_produk']};"
            f"{data_produk['nama_produk']};"
            f"{data_produk['harga_produk']};"
            f"{data_produk['stok_produk']}\n"
        )

def baca_stok(): # membaca isi data/produk.txt
    daftar_produk= []
    try:
        with open("data/produk.txt", "r", encoding="utf-8") as file: # Membaca isi file
            for baris in file:
                bagian = baris.strip().split(";")
                
                if len(bagian) != 4:
                    print("Data Rusak, baris dilewati")
                    continue
                
                try:
                    data_produk = {
                        "kode_produk":bagian[0],
                        "nama_produk":bagian[1],
                        "harga_produk":float(bagian[2]),
                        "stok_produk":int(bagian[3])
                    }
                    daftar_produk.append(data_produk)

                except ValueError:
                    print("Harga atau stok tidak Valid, baris dilewati")
    except FileNotFoundError:
        print("File data/produk.txt belum ditemukan. Silakan tambahkan produk terlebih dahulu.")
        return []
    return daftar_produk

def tulis_ulang_stok(daftar_produk): # Menulis ulang seluruh data produk setelah ada perubahan stok.
    with open("data/produk.txt", "w", encoding="utf-8") as file: # Mode w menimpa isi file dengan data terbaru.
        for produk in daftar_produk:
            file.write(
                f"{produk['kode_produk']};"
                f"{produk['nama_produk']};"
                f"{produk['harga_produk']};"
                f"{produk['stok_produk']}\n"
            )
# Mencari produk berdasarkan kode tanpa membedakan huruf besar dan kecil.
def cari_produk(daftar_produk, kode_produk): # Proses Mencari Produk
    for produk in daftar_produk:
        if produk["kode_produk"].lower() == kode_produk.lower():
            return produk

    return None

def buat_ringkasan(**data): # Mengumpulkan data ringkasan menggunakan keyword arguments.
    return data

def hitung_total_nilai_stok(*harga_stok): # Proses Menghitung seluruh harga berdasarkan seluruh produk menggunakan *args
    return sum(harga_stok)

def hitung_nilai_stok(daftar_produk): # Proses menghitung seluruh harga berdasarkan 1 produk
    nilai_produk = []

    for produk in daftar_produk:
        nilai = produk['harga_produk'] * produk['stok_produk']
        nilai_produk.append(nilai)

    return hitung_total_nilai_stok(*nilai_produk)
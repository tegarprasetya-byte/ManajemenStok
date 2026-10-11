def validasi_kode_produk(kode_produk): # Memastikan kode produk berupa teks dan tidak kosong.
    #mengvalidari kode produk
    if not isinstance(kode_produk, str):
        raise ValueError("Kode Produk harus berupa teks")
    if not kode_produk.strip():
        raise ValueError("Kode Produk tidak boleh kosong")

    return kode_produk.strip()

def validasi_harga(harga):
# Memastikan harga dapat dikonversi menjadi angka positif.
    #mengvalidasi harga harus float
    try:
        harga_desimal = float(harga)
    except (ValueError,TypeError):
        raise ValueError("Harga Harus Berupa Angka Desimal")

    if harga_desimal <= 0:
        raise ValueError("Harga Harus berupa angka positif")

    return harga_desimal

def validasi_stok(stok):# Memastikan stok berupa bilangan bulat dan tidak negatif.
    #mengvalidasi stok harus bilangan bulat
    try:
        valid_stok = int(stok)
    except (ValueError,TypeError):
        raise ValueError("Stok Harus Berupa Bilangan Bulat")
    
    if valid_stok < 0:
        raise ValueError("Stok tidak boleh negatif")

    return valid_stok

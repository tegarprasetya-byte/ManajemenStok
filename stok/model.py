
class Produk:
    # Menyimpan informasi satu produk.
    def __init__(self, kode_produk, nama_produk, harga_produk, stok_produk):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.harga_produk = float(harga_produk)
        self.stok_produk = int(stok_produk)

    # Menghitung nilai stok satu produk.
    def hitung_nilai_stok(self):
        return self.harga_produk * self.stok_produk

    # Mengubah data produk menjadi dictionary.
    def ke_dict(self):
        return {
            "kode_produk": self.kode_produk,
            "nama_produk": self.nama_produk,
            "harga_produk": self.harga_produk,
            "stok_produk": self.stok_produk
        }


class ManajemenStok:
    # Menyimpan dan mengelola daftar produk.
    def __init__(self, daftar_produk=None):
        self.daftar_produk = daftar_produk or []

    # Menambahkan produk ke daftar.
    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)

    # Menghitung nilai seluruh stok.
    def hitung_total_nilai_stok(self):
        return sum(
            produk.hitung_nilai_stok()
            for produk in self.daftar_produk
        )

    # Mengurutkan produk berdasarkan harga menggunakan lambda.
    def urutkan_produk_berdasarkan_harga(self):
        return sorted(
            self.daftar_produk,
            key=lambda produk: produk.harga_produk
        )

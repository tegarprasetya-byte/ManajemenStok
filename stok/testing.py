import unittest
import os

from stok.validasi import (
    validasi_kode_produk,
    validasi_harga,
    validasi_stok
)
from main import laporan_stok

from stok.processing import (
    cari_produk,
    hitung_total_nilai_stok,
    hitung_nilai_stok
)


class TestManajemenStok(unittest.TestCase):

    def test_kode_produk_valid(self):
        self.assertEqual(
            validasi_kode_produk("P001"),
            "P001"
        )

    def test_harga_valid(self):
        self.assertEqual(
            validasi_harga("15000"),
            15000.0
        )

    def test_harga_tidak_valid(self):
        with self.assertRaises(ValueError):
            validasi_harga("abc")

    def test_stok_valid(self):
        self.assertEqual(
            validasi_stok("10"),
            10
        )

    def test_stok_negatif(self):
        with self.assertRaises(ValueError):
            validasi_stok("-5")

    
def test_cari_produk(self):
    daftar = [
        {
            "kode_produk": "P001",
            "nama_produk": "Buku",
            "harga_produk": 10000,
            "stok_produk": 5
        }
    ]

    hasil = cari_produk(daftar, "P001")
    self.assertEqual(hasil["nama_produk"], "Buku")


def test_hitung_nilai_stok(self):
    daftar = [
        {
            "kode_produk": "P001",
            "nama_produk": "Buku",
            "harga_produk": 10000,
            "stok_produk": 2
        },
        {
            "kode_produk": "P002",
            "nama_produk": "Pulpen",
            "harga_produk": 5000,
            "stok_produk": 3
        }
    ]

    self.assertEqual(hitung_nilai_stok(daftar), 35000)


    def test_hitung_total(self):
        self.assertEqual(
            hitung_total_nilai_stok(10000, 20000, 5000),
            35000
        )

class TestLaporanStok(unittest.TestCase):

    def test_laporan_stok_dibuat(self):
        nama_file = "laporan/laporan_stok.txt"

        # Pastikan folder data sudah tersedia
        self.assertTrue(os.path.isdir("laporan"))

        # Periksa file laporan setelah fitur dijalankan
        laporan_stok()

        self.assertTrue(os.path.exists(nama_file))

    def test_isi_laporan_stok(self):
        nama_file = "laporan/laporan_stok.txt"

        laporan_stok()

        with open(nama_file, "r", encoding="utf-8") as file:
            isi = file.read()

        self.assertIn("LAPORAN STOK PRODUK", isi)
        self.assertIn("Total nilai stok", isi)


if __name__ == "__main__":
    unittest.main()

"""Latihan 1: Iterasi dan Kalkulasi
Diberikan dictionary harga buah: harga_buah = {"apel": 5000, "jeruk": 8500, "mangga":
7800, "pisang": 3000}.
Gunakan for loop dan .items() untuk mencetak setiap buah dan harganya dalam format "Harga 1 kg
[nama buah] adalah Rp [harga]". Di akhir, hitung dan cetak total harga semua buah.


Latihan 2: Manajemen Kontak
Buat program manajemen kontak sederhana:
-. Buat dictionary kosong bernama kontak.
/. Tambahkan tiga kontak (misal: "Ibu", "Ayah", "Teman") beserta nomor teleponnya.
0. Ubah nomor telepon "Ibu".
1. Gunakan .pop() untuk menghapus "Teman".
3. Cetak dictionary kontak akhir.


Latihan 3: Nested Dictionary
Buatlah sebuah nested dictionary untuk menyimpan data dua produk di sebuah toko online.
Key utamanya adalah ID produk (misal: "PROD001", "PROD002").
Setiap produk harus memiliki key untuk "nama", "harga", dan "stok".
Setelah membuatnya, tulis kode untuk mencetak nama dan harga dari produk dengan ID "PROD002".


Latihan 4: Frekuensi Hari
Tulis program yang membaca file mbox-short.txt. Bangun histogram menggunakan dictionary untuk
menghitung berapa banyak pesan yang dikirim pada setiap hari dalam seminggu. (Lihat baris yang dimulai
dengan "From ", kata ketiganya adalah hari). Cetak dictionary hasilnya."""

#Latihan 1
harga_buah = {
    "apel": 5000,
    "jeruk": 8500,
    "mangga": 7800,
    "pisang": 3000
}

total_harga = 0
for buah, harga in harga_buah.items():
    print(f"Harga 1 kg {buah} adalah Rp {harga}")
    total_harga += harga
print("Total harga semua buah:", total_harga)


# Latihan 2
kontak = {}

# Tambah 3 kontak
kontak["Ibu"] = "08123456789"
kontak["Ayah"] = "08234567890"
kontak["Teman"] = "08345678901"

# Ubah nomor telepon Ibu
kontak["Ibu"] = "08987654321"

# Hapus Teman
kontak.pop("Teman")

print("Kontak akhir:", kontak)


# Latihan 3
produk = {
    "PROD001": {
        "nama": "Laptop",
        "harga": 7500000,
        "stok": 5
    },
    "PROD002": {
        "nama": "Smartphone",
        "harga": 3500000,
        "stok": 10
    }
}

print("Nama produk PROD002:", produk["PROD002"]["nama"])
print("Harga produk PROD002:", produk["PROD002"]["harga"])


# Latihan 4
import os

# Pastikan Python bekerja di folder yang sama dengan file .py ini
os.chdir(os.path.dirname(__file__))

histogram_hari = {}

try:
    with open("mbox-short.txt") as file:
        for baris in file:
            if baris.startswith("From "):
                kata = baris.split()
                hari = kata[2]  # kata ke-3 adalah hari
                histogram_hari[hari] = histogram_hari.get(hari, 0) + 1
except FileNotFoundError:
    print("File 'mbox-short.txt' tidak ditemukan.")

print("Frekuensi pesan per hari:", histogram_hari)
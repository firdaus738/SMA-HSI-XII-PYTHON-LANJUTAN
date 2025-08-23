"""Latihan 1: Membuat dan Mengakses
-. Buat sebuah dictionary bernama biodata untuk merepresentasikan dirimu. Isinya harus memiliki
key: "nama", "umur", "hobi" (hobi bisa berupa list dari beberapa string), dan
"sudah_menikah" (berisi boolean).
/. Cetak seluruh dictionary.
0. Cetak hanya value dari key "nama".
1. Cetak hobi pertamamu dari list hobi.
Latihan 2: Modifikasi Dictionary
-. Gunakan dictionary biodata dari Latihan 1.
/. Tambahkan pasangan key-value baru: "kota": "Nama Kotamu".
0. Ubah value dari key "umur" menjadi umurmu tahun depan.
1. Cetak dictionary yang sudah diperbarui.
Latihan 3: Penggunaan .get()
-. Masih dengan dictionary biodata.
/. Coba akses key "pekerjaan" menggunakan bracket notation []. Apa yang terjadi? (Beri komentar
pada baris ini agar tidak error).
0. Sekarang, akses key "pekerjaan" menggunakan metode .get(). Cetak hasilnya.
1. Akses lagi key "pekerjaan" menggunakan .get(), tapi kali ini berikan nilai default "Pelajar".
Cetak hasilnya.
Latihan 4: Histogram Kata
Buat program yang:
-. Meminta pengguna memasukkan sebuah kalimat.
/. Membuat histogram (dalam bentuk dictionary) yang menghitung frekuensi setiap kata (bukan
huruf) dalam kalimat tersebut.
0. Cetak dictionary histogram tersebut.
Petunjuk: Gunakan metode .split() untuk mengubah kalimat menjadi list kata-kata terlebih
dahulu. Abaikan huruf besar/kecil dengan mengubah seluruh kalimat menjadi lowercase di awal."""



# ===== Latihan 1: Membuat dan Mengakses =====
biodata = {
    "nama": "Muhammad Firdaus Abdurrohim",
    "umur": 17,
    "hobi": ["ngoding", "desain", "main bola"],
    "sudah_menikah": False
}

# Cetak seluruh dictionary
print("Biodata lengkap:", biodata)

# Cetak value dari key "nama"
print("Nama:", biodata["nama"])

# Cetak hobi pertama
print("Hobi pertama:", biodata["hobi"][0])

# ===== Latihan 2: Modifikasi Dictionary =====
biodata["kota"] = "Sukabumi"  # Tambah key-value baru
biodata["umur"] += 1          # Ubah umur jadi tahun depan
print("Biodata setelah update:", biodata)

# ===== Latihan 3: Penggunaan .get() =====
# print(biodata["pekerjaan"])  # Contoh pakai bracket → ERROR kalau key tidak ada

# Akses key "pekerjaan" pakai .get()
print("Pekerjaan:", biodata.get("pekerjaan"))

# Akses key "pekerjaan" pakai .get() dengan nilai default
print("Pekerjaan (default):", biodata.get("pekerjaan", "Pelajar"))

# ===== Latihan 4: Histogram Kata =====
kalimat = input("Masukkan sebuah kalimat: ").lower()
kata_list = kalimat.split()

histogram = {}
for kata in kata_list:
    histogram[kata] = histogram.get(kata, 0) + 1

print("Histogram kata:", histogram)
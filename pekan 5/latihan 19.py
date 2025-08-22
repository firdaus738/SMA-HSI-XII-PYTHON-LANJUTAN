

import re

# Latihan 1
data = "Pendapatan bulan ini adalah Rp 1,500,000, sedangkan pengeluaran sebesar Rp 850,000."
angka = re.findall(r"\d+", data)
print(angka)

# Latihan 2
nomor = input("Masukkan nomor telepon: ")
if re.search(r"^\d+$", nomor) and 10 <= len(nomor) <= 13:
    print("Format nomor telepon valid.")
else:
    print("Format tidak valid.")
print(r"Pola yang mungkin: ^\d+$ (ini hanya mengecek apakah semuanya digit, dan perlu tambah len())")

# Latihan 3
teks = "python adalah bahasa yang menyenangkan, python mudah dipelajari."
cari_search = re.search(r"python", teks)
print("re.search() ->", cari_search.group())
cari_findall = re.findall(r"python", teks)
print("re.findall() ->", cari_findall)

# Latihan 4
kalimat = "Kucing, anjing, dan burung adalah hewan peliharaan."
kata_g = re.findall(r"\b\w+g\b", kalimat)
print(kata_g)
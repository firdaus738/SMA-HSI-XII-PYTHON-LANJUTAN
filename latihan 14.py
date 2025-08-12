"""Latihan 1: Manajemen Daftar Belanja
-. Buat sebuah list kosong bernama belanjaan.
/. Gunakan .append() untuk menambahkan "Telur", "Susu", dan "Roti".
0. Gunakan .insert() untuk menambahkan "Apel" di posisi paling awal.
1. Gunakan .remove() untuk menghapus "Susu".
3. Cetak list akhir. 


Latihan 2: Mengurutkan Tanpa Mengubah
-. Buat list nilai = [98, 76, 88, 100, 54].
/. Gunakan fungsi sorted() untuk mendapatkan versi terurut dari list tersebut dan simpan di
variabel baru.
0. Cetak list nilai yang asli (pastikan ia tidak berubah).
1. Cetak list baru yang sudah terurut.


Latihan 3: Analisis Kata
Buat program yang:
-. Meminta pengguna memasukkan sebuah kalimat.
/. Gunakan .split() untuk mengubah kalimat tersebut menjadi sebuah list kata-kata.
0. Gunakan len() untuk menghitung dan mencetak jumlah kata dalam kalimat.
1. Gunakan .sort() pada list tersebut untuk mengurutkan kata-kata berdasarkan abjad, lalu cetak
list yang sudah terurut.


Latihan 4: Memahami Aliasing
Prediksikan output dari kode di bawah ini sebelum menjalankannya. Jelaskan mengapa outputnya seperti
itu.
a = [1, 2, 3, 4, 5]
b = a
c = a.copy()
b[1] = 20
c[1] = 30
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")"""


#1
belanjaan = []

belanjaan.append("Telur")
belanjaan.append("Susu")
belanjaan.append("Roti")

belanjaan.insert(0, "Apel")

belanjaan.remove("Susu")

print("Daftar belanja:", belanjaan)

#2
nilai = [98, 76, 88, 100, 54]

nilai_urut = sorted(nilai)

print("Nilai asli:", nilai)
print("Nilai terurut:", nilai_urut)

#3
kalimat = input("Masukkan sebuah kalimat: ")

kata_kata = kalimat.split()

print("Jumlah kata:", len(kata_kata))

kata_kata.sort()

print("Kata-kata terurut:", kata_kata)

#4
a = [1, 2, 3, 4, 5]
b = a           
c = a.copy()    

b[1] = 20     
c[1] = 30       
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
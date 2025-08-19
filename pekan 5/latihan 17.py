"""Latihan 1: Sintaks Tuple
-. Buatlah sebuah tuple bernama hari yang berisi nama-nama hari dari Senin sampai Minggu.
/. Buatlah sebuah tuple bernama angka_ganjil yang hanya berisi satu angka: 7. Pastikan tipenya
benar-benar tuple.
0. Cetak kedua tuple dan tipe datanya.


Latihan 2: Immutability
Diberikan tuple koordinat_awal = (10, 20). Tulis kode yang menghasilkan tuple baru bernama
koordinat_baru yang nilainya (10, 25). Kamu tidak boleh mengubah koordinat_awal secara
langsung.


Latihan 3: Tuple Assignment
Sebuah fungsi mengembalikan informasi RGB sebuah warna sebagai tuple: warna = (255, 165, 0).
Gunakan tuple assignment untuk "membongkar" nilai tersebut ke dalam tiga variabel terpisah: red, green,
dan blue. Cetak ketiga variabel tersebut.


Latihan 4: Dictionary dengan Tuple Key
Buatlah sebuah dictionary bernama papan_catur. Gunakan tuple (baris, kolom) sebagai key
untuk menyimpan nama bidak catur. Contoh:
papan_catur[(1, 'a')] = "Benteng Putih"
papan_catur[(8, 'h')] = "Benteng Hitam"
Isi beberapa posisi, lalu akses dan cetak bidak yang ada di posisi (1, 'a')."""

#1
# Tuple nama-nama hari
hari = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu")

# Tuple satu elemen (jangan lupa koma!)
angka_ganjil = (7,)

# Cetak isi dan tipe data
print("Tuple hari:", hari, type(hari))
print("Tuple angka_ganjil:",)
      
#2
koordinat_awal = (10, 20)

# Membuat tuple baru (tidak mengubah yang lama)
koordinat_baru = (koordinat_awal[0], 25)

print("Koordinat awal:", koordinat_awal)
print("Koordinat baru:", koordinat_baru)

#3
warna = (255, 165, 0)

# Membongkar tuple ke variabel
red, green, blue = warna

print("Red:", red)
print("Green:", green)
print("Blue:", blue)

#4
papan_catur = {}

# Isi beberapa posisi
papan_catur[(1, 'a')] = "Benteng Putih"
papan_catur[(1, 'b')] = "Kuda Putih"
papan_catur[(8, 'h')] = "Benteng Hitam"

# Akses posisi tertentu
print("Isi papan:", papan_catur)
print("Bidak di (1, 'a'):", papan_catur[(1, 'a')])

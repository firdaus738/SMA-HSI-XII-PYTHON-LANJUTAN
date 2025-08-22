# ============================================
#  SELAMAT DATANG DI APLIKASI POLLING
# ============================================

# Struktur data survei
SURVEI = [
    {
        "pertanyaan": "Apa bahasa pemrograman favoritmu?",
        "opsi": ["Python", "JavaScript", "Java", "C++"]
    },
    {
        "pertanyaan": "Apa sistem operasi yang paling sering kamu gunakan?",
        "opsi": ["Windows", "macOS", "Linux"]
    },
    {
        "pertanyaan": "Tim mana yang akan menang di final piala dunia?",
        "opsi": ["Argentina", "Prancis", "Brasil", "Jerman"]
    }
]

# Inisialisasi hasil polling
hasil_polling = {}
for item_survei in SURVEI:
    for opsi in item_survei["opsi"]:
        hasil_polling[opsi] = 0

# Loop utama: tanyakan setiap pertanyaan
for i, item_survei in enumerate(SURVEI, start=1):
    print(f"\nPertanyaan {i}: {item_survei['pertanyaan']}")
    for opsi in item_survei["opsi"]:
        print(f" - {opsi}")

    # Validasi input
    while True:
        jawaban = input("Jawaban Anda: ")
        if jawaban in item_survei["opsi"]:
            print(f"> {jawaban}")
            print("--- Terima kasih! ---")
            hasil_polling[jawaban] += 1
            break
        else:
            print("Jawaban tidak valid. Silakan pilih dari opsi yang tersedia.")

# Menampilkan hasil polling
print("\n============================================")
print(" HASIL POLLING")
print("============================================")

total_suara = sum(hasil_polling.values())

for opsi, jumlah in hasil_polling.items():
    if total_suara > 0:
        persentase = (jumlah / total_suara) * 100
    else:
        persentase = 0
    print(f"{opsi} : {jumlah} suara ({persentase:.2f}%)")

print("============================================")

# BONUS: Simpan hasil ke file
with open("hasil_polling.txt", "w", encoding="utf-8") as f:
    f.write("=== HASIL POLLING ===\n")
    for opsi, jumlah in hasil_polling.items():
        persentase = (jumlah / total_suara) * 100 if total_suara > 0 else 0
        f.write(f"{opsi} : {jumlah} suara ({persentase:.2f}%)\n")

print("Hasil polling telah disimpan ke 'hasil_polling.txt'")
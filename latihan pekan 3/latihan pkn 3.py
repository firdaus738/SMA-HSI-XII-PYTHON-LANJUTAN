import os

# Pastikan Python bekerja di folder yang sama dengan file .py ini
os.chdir(os.path.dirname(__file__))

try:
    # Buka file input
    with open("transaksi_kotor.txt", "r") as file_input:
        # Buka file output
        with open("laporan_bersih.txt", "w") as file_output:
            # Tulis header laporan
            file_output.write("LAPORAN TRANSAKSI BERSIH\n")
            file_output.write("=========================\n")

            grand_total = 0  # Total keseluruhan

            for baris in file_input:
                # Lewati baris kosong
                if not baris.strip():
                    continue

                # Bersihkan dan pecah data
                data_potongan = baris.strip().split(",")

                # Ambil dan bersihkan setiap bagian
                id_transaksi = data_potongan[0].strip().upper()
                nama_produk = data_potongan[1].strip().title()
                jumlah = int(data_potongan[2].strip())
                harga_satuan = float(data_potongan[3].strip())

                # Hitung total harga
                total_harga = jumlah * harga_satuan
                grand_total += total_harga

                # Tulis ke file output
                file_output.write(
                    f"ID: {id_transaksi} | Produk: {nama_produk} | Jumlah: {jumlah} | Total Harga: Rp {total_harga:,.2f}\n"
                )

            # Footer
            file_output.write(f"--- ANALISIS SELESAI ---\n")
            file_output.write(f"TOTAL KESELURUHAN: Rp {grand_total}\n")

    print("Proses pembersihan data selesai. Laporan disimpan di laporan_bersih.txt")

except FileNotFoundError:
    print("File transaksi_kotor.txt tidak ditemukan. Pastikan file ada di folder yang sama.")
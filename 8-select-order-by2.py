import sqlite3
koneksi = sqlite3.connect('db_fauna.db')
kursor = koneksi.cursor()

kursor.execute("SELECT * FROM Fauna ORDER BY jml_sekarang DESC")
baris_tabel = kursor.fetchall()

print("Data Fauna pada 2023")
print("="*110)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID", "Nama_Fauna", "Jenis", "Asal", "jml_Sekarang", "thn_ditemukan"))
print("-"*110)

for baris in baris_tabel:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

koneksi.close()

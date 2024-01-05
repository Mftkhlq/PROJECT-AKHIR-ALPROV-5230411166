import sqlite3
koneksi = sqlite3.connect('db_fauna.db')

kursor = koneksi.cursor()

kursor.execute("SELECT SUM(Jml_sekarang) FROM Fauna ")
jml_fauna = kursor.fetchall()[0] 

print(f"jumlah Total Hewan saat ini Adalah: {jml_fauna}")
koneksi.close()
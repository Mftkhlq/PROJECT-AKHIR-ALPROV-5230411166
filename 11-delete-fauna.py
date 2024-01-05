import sqlite3
koneksi = sqlite3.connect('db_fauna.db')
kursor = koneksi.cursor()

def tampilkan_data_sebelum():
    kursor.execute("SELECT * FROM Fauna")
    data_sebelum = kursor.fetchall()

    print("Data sebelum Pengahapusan:")
    for row in data_sebelum:
        print(row)

   #  koneksi.close()

def tampilkan_data_sesudah():
    kursor.execute("DELETE FROM Fauna WHERE asal = 'Kalimantan' ")
    
    kursor.execute("SELECT * FROM Fauna")
    data_sesudah = kursor.fetchall()

    print("Data Sesudah Penghapusan:")
    for row in data_sesudah:
        print(row)

    koneksi.close()

tampilkan_data_sebelum()

tampilkan_data_sesudah()
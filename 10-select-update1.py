import sqlite3
koneksi = sqlite3.connect('db_fauna.db')
kursor = koneksi.cursor()

id_fauna = 10
jml_Sekarang_baru = 650

kursor.execute(f"UPDATE Fauna SET jml_sekarang = {jml_Sekarang_baru} WHERE id_fauna = {id_fauna}")
koneksi.commit()

print("DATA HEWAN INDONESIA 2023")
if kursor.rowcount > 0:
    print(f"Data KATAK BORNEO Dengan ID {id_fauna} Berhasil Di Ubah!")
else:
    print(f"tidak ada data FAUNA dengan id {id_fauna}")

koneksi.close()

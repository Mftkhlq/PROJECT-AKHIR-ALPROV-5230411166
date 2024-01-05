import sqlite3

koneksi = sqlite3.connect('db_fauna.db')

koneksi.execute('''
             CREATE TABLE Fauna(
                id_fauna INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_fauna VARCHAR(50),
                jenis VARCHAR(50),
                asal VARCHAR(50),
                jml_sekarang INTEGER(10),
                thn_ditemukan INTEGER(10)
            )
            ''')
koneksi.close()

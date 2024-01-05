import sqlite3
koneksi = sqlite3.connect('db_fauna.db')

koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_sekarang, thn_ditemukan)
                VALUES('harimau jawa', 'mamalia', 'jawa', '40', '2019' )
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_sekarang, thn_ditemukan)
                VALUES('kuskus beruang', 'mamalia', 'sulawesi', '30', '2021' )
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_sekarang, thn_ditemukan)
                VALUES('beruang madu', 'mamalia', 'sumatra', '1000', '2020' )
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_sekarang, thn_ditemukan)
                VALUES('pesut mahakam', 'mamalia', 'kalimantan', '100', '2021' )
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_sekarang, thn_ditemukan)
                VALUES('burung maleo', 'burung', 'sulawsi', '7000', '2023' )
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_sekarang, thn_ditemukan)
                VALUES('macan dahan', 'mamalia', 'sumatra', '400', '2020' )
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_sekarang, thn_ditemukan)
                VALUES('kancil', 'mamalia', 'jawa', '60', '2022' )
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_sekarang, thn_ditemukan)
                VALUES('gajah kalimantan', 'mamalia', 'kalimantan', '1500', '2021' )
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_sekarang, thn_ditemukan)
                VALUES('elang jawa', 'burung', 'jawa', '200', '2021' )
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_sekarang, thn_ditemukan)
                VALUES('katak borneo', 'amfibi', 'kalimantan', '2000', '2023' )
                ''')
koneksi.commit()
koneksi.close()

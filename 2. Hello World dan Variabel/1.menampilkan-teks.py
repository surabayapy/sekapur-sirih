#!/usr/bin/env python3

from surabaya import pemisah_baris

# Ini adalah komentar, tidak akan ditampilkan
# Komentar dilakukan dengan memberi tanda pagar sebelum komentar

# Cara menampilkan teks
# Coba cari perbedaan dari dua perintah dibawah dan lihat hasil outputnya
print('')
print('Hello World')
print("Hello World")
print('')

# Perhatikan juga hal ini
print('Surabaya.py mengucapkan "Selamat Datang!"')
print("Surabaya.py mengucapkan 'Selamat Datang!'")

# Sedikit pemisah, lihat bagaimana hal ini ditampilkan
print('') # Coba bedakan ini
print('*'*5 + '#'*10 + '*'*5) # berapa kali # dan * ditampilkan?
print('\n') # dengan ini
# Tiga perintah diatas selanjutnya akan diganti dengan perintah 'pemisah_baris()'


# Menggunakan Variabel
# Kita akan menggunakan sebuah variabel dengan nama 'nama' dan isinya 'Donny'
nama = 'Donny'
print('nama')
print(nama)
print('nama ' + nama)

# Dua hal dibawah ini tidak akan bisa dijalankan, uncomment dan cari tau kenapa
# print(Nama)
# print(NAMA)

pemisah_baris()

# Dengan variabel yang sama, mari kita ubah
nama = 'bukan donny'
print(nama.title()) # variabel nama dengan gaya 'Title'
print(nama.lower())
print(nama.upper())
print(nama) # variabel nama sebenarnya tidak berubah

pemisah_baris()

# 
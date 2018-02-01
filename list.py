from fungsi import pembuka             #import fungsi pembuka() pada file fungsi.py
from fungsi import pemisah_baris       #import fungsi pemisah_baris() pada file fungsi.py


pembuka()                              #kata pembuka pada file fungsi.py


#beberapa fungsi dan methods untuk list


kita = ['aku', 'kamu', 'mereka']       #misal ada list dengan nama 'kita'


#untuk mengganti elemen pada list
kita[0] = 'saya'                       #elemen pada index 0 diganti dengan kata 'saya'
print(kita)                            #lihat perubahannya

pemisah_baris()                        

#untuk menambah elemen pada list
kita.append('dia')                     #menambahkan kata 'dia' pada list
print(kita)                            #lihat perubahannya

pemisah_baris()                        

#menambahkan elemen pada list pada index yang dapat kita tentukan
kita.insert(2, 'kalian')
print(kita)

pemisah_baris()                        

#remove item menggunakan perintah del
del kita[2]
print(kita)

pemisah_baris()

#mengambil sekaligus menghapus item dalam list menggunakan pop()
popped_kita = kita.pop(2)
print(popped_kita)
print(kita)

pemisah_baris()

#menghapus item dengan value (nilai) pada list
kita.remove('saya')
print(kita)

pemisah_baris()

#mengurutkan item list sesuai dengan abjad (A - Z)
kita.sort()
print(kita)

pemisah_baris()

#mengurutkan item list sesuai dengan abjad (Z - A)
kita.sort(reverse=True)         
#bisa juga seperti ini --> kita.reverse()
print(kita)

pemisah_baris()

#mengurutkan item list hanya sementara
print(sorted(kita))
print(kita)

pemisah_baris()

#untuk mengetahui index elemen pada list, bisa menggunakan method .index('elemen')
print(kita.index('kamu'))

pemisah_baris()

#untuk mengetahui banyaknya item pada list 
print(len(kita))

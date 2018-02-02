from fungsi import pemisah_baris          #dari file fungsi.py import fungsi pemisah baris
from fungsi import pembuka                #dari file fungsi.py import fungsi pembuka

pembuka()                                 #fungsi pembuka
pemisah_baris()                           #fungsi pemisah_baris

print('hello world ! :')
print("kata orang, programmer itu harus bisa 'hello world!'")

pemisah_baris()

#variable
print('variable :')
variable = 'aku variable'
print(variable)

pemisah_baris()

#list
print('list :')
nomor = [1, 2, 3, 4, 5]
print(nomor)

pemisah_baris()

#tuples
print('tuples :')
toples = (1, 2, 3, 4)
print(toples)

pemisah_baris()

#dictionary
print('dictionary :')
dunia = {'indo':1, 'malay':3, 'china':2}
ranking_indo = dunia['indo']
ranking_malay = dunia['malay']
print('ganda campuran dari indonesia meraih ranking :' + str(ranking_indo))
print('sedangkan ganda campuran dari malaysia meraih ranking :' + str(ranking_malay))

dunia['jerman'] = 8     #menambahkan dictionary baru
print(dunia)

del dunia['china']      #menghapus item dictionary
print(dunia)

pemisah_baris()

#if statement
print('if statement :')
umur = 12

if umur < 4:
    harga = 'Rp. 3000,-'

elif umur < 18:
    harga = 'Rp. 5000,-'

else:
    harga = 'Rp. 10.000'

print("harga tiket yang harus dibayar adalah :" + harga + '.')

pemisah_baris()

#looping
print('looping :')
for black in toples:
    print('ini tuple ke : ' + str(black))

pemisah_baris()


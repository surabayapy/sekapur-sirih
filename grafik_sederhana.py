import matplotlib.pyplot as plt #pastikan kamu telah menginstall matplotlib
#cara install matplotlib -->   pip3 install matplotlib

tahun = [1920, 1940, 1960, 1980] #list tahun
nilai = [2.42, 2.56, 2.67, 3.55] #list nilai

plt.plot(tahun, nilai) #menampilkan list tahun1 sebagai sumbu x dan nilai1 sebagai y

plt.xlabel('tahun') #ngasih judul pada sumbu x 
plt.ylabel('nilai') #ngasih judul pada sumbu y
plt.title('nilai matematika sd huruhara') #judul grafik
plt.yticks([0, 1, 2, 3, 4, 5]) #mengatur batas sumbu y

plt.show() #method buat nampilin grafiknya. kalo ga jalanin baris ini, maka grafiknya gaakan muncul haha

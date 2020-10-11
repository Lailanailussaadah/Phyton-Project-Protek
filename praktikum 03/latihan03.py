# import library
import time
import datetime

#input nama user
nama = input ("Hello... nama saya Mr. Kompie, nama anda siapa? ")

#tampilkan nama user
print ("Oh... nama Anda, nama", ", nama yang bagus sekali.")

#kasih jeda 3 detik
time. sleep (3)

#input tahun lahir
thnLahir = int(input("BTW..." + nama + "kamu lahir tahun berapa?"))

#kasih jeda 3 detik
time. sleep(3)

#hitung usia user
skrg = datetime. datetime. now()
usia = skrg.year - thnLahir

#tampilkan usia
print ("Hmm...", nama,"kamu sudah", usia, "tahun ya...")

#kasih jeda 3 detik
time. sleep (3)

#tampilkan pesan sesuai range usia
if (usia > 50):
    print ("Anda sudah cukup tua ya?")
    print ("jaga kesehatan ya!!")
elif (usia > 20):
    print ("ternyata Anda masih cukup muda belia")
    print ("jangan sia-siakan ,asa mudamu ya!!")
elif (usia > 17):
    print (" hihihi... Anda ternyata ,asih ABG")
    print ("Mulai berpikirlah secara dewasa ya!!")
else :
    print ("Oalah... Anda masih ana-anak toh?")
    print ("Jadilah suka merengek-rengek minta jajan ya !!")

#kasih jeda 3 detik
    time. sleep (3)

#say goodbye
print ("Ok... see you later", nama, "...senang berkenalan denganmu")

            
              

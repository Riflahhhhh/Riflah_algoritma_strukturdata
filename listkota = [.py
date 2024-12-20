#listt
listkota = [
    'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo', 'Yogyakarta', 'Semarang', 'Makassar'
]
for kota in listkota:
    print(kota)

#fordenganfungsirange
## 0 sampai 4
for i in range(5):
    print("Perulangan ke -",i)
    
for i in range(100):
    print("Sebut angka ke -",i)

### Mencari Bilangan Ganjil
for bilangan_ganjil in range (1,100,2):
    print(bilangan_ganjil)
for bilangan_genap in range (0,100,2):
    print(bilangan_genap)

#for dengan tuple
tuplebuah = ('Semangka', 'Mangga', 'Melon', 'Stroberi')
for buah in tuplebuah:
    print(buah)

#forelse
listkota = [
    'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo', 'Yogyakarta', 'Semarang', 'Makassar'
]
for kota in listkota:
    print(kota)
else:
    print('Tidak ada lagi item yang tersisa')

listkota = [
    'Jambi', 'Sulawesi', 'Denpasar', 'Bogor', 'Madura', 'Bangka', 'Surakarta', 'Medan'
]
for kota in listkota:
    print(kota)
else:
    print('Semua kota telah ditampilkan')

#for...else + break
listkota = [
    'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo', 'Yogyakarta', 'Semarang', 'Makassar'
]
kotayangdicari = input('Ketik nama kota yang kamu cari: ')
for i, kota in enumerate(listkota):
    # kita ubah katanya ke lowercase agar
    # menjadi case insensitive
    if kota.lower() == kotayangdicari.lower():
        print('kota yang anda cari berada pada indkes', i)
        break
else:
    print('maaf, kota yang anda cari tidak ada')
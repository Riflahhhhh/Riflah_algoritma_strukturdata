#PERULANGAN WHILE

listkota = [
    'Jakarta', 'Surabaya', ' Medan', 'Belitung', 'Jambi', 'Makassar', ' Solo'
]

#bermain index
i = 0
while i < len(listkota):
    print(listkota)
    i += 1

#PERULANGAN WHILE DENGAN INPUTAN
a = int(input('Masukkan bilangan ganjil lebih dari 50: '))

while a % 2 != 1 or a <= 50:
    a = int(input('Salah, masukkan lagi: '))

print('benar')

#PERULANGAN DENGAN CONTINUE
listkota = [
    'Jakarta', 'Bandung', 'Surabaya', 'Medan', 'Maluku', 'Aceh'
]

Kotayangdicari = input('Masukkan nama Kota yang dicari:')

i = 0
while i < len(listkota):
    if listkota[i].lower() == kotayangdicari.lower():
        print('ketemu di index:', i)
        break
    
    print('Bukan', listkota[i])
    i += 1
else:
    print ('Maaf, kota yang anda cari tidak ditemukan.')
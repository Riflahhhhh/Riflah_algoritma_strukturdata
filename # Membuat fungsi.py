# Membuat fungsi
def salam():
    print ("Hello, selamat pagi")

## Pemanggilan fungsi
salam()
salam()
salam()

# Membuat fungsi dengan parameter
def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print ("luas segitiga: %f" % luas)

#Pemanggilan fungsi
luas_segitiga(4,6)

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

#Pemanggilan fungsi
print ("Luas persegi: %d" % luas_persegi(6))

#rumus sisi * sisi
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas
#rumus sisi * sisi * sisi
def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
    return volume
sisi = 10
print("luas persegi:", luas_persegi(sisi))
print("volume kubus:", volume_persegi(sisi))

#membuat variabel global
nama = "Belajar kode"
versi = "1.0.1"

def help():
    #ini variabel lokal
    nama = "Programku"
    versi = "1.0.1"
    #mengakses variabel global
    print ("nama: %s" % nama)
    print ("versi: %s" % versi)

#mengakses variabel global
print ("nama: %s" % nama)
print ("versi: %s" % versi)

#memanggil fungsi help()
help()

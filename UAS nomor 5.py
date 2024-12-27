# Masukkan usia langsung dalam kode
usia = 20  # Ganti angka ini dengan usia yang ingin diuji

# Menentukan kategori usia menggunakan percabangan
if usia >= 0 and usia <= 5:
    kategori = "Balita"
elif usia >= 6 and usia <= 12:
    kategori = "Anak-anak"
elif usia >= 13 and usia <= 17:
    kategori = "Remaja"
elif usia >= 18 and usia <= 59:
    kategori = "Dewasa"
elif usia >= 60:
    kategori = "Lansia"
else:
    kategori = "Usia tidak valid"

# Menampilkan kategori usia
print(f"Kategori usia Anda adalah: {kategori}")

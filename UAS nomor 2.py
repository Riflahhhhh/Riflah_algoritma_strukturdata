# Fungsi untuk mencetak pola bintang segitiga
def cetak_pola(baris):
    for i in range(1, baris + 1):
        # Mencetak bintang sesuai jumlah baris dan urutan baris
        print('*' * i)

# Masukkan jumlah baris langsung dalam kode
baris = 5  # Ganti angka ini dengan jumlah baris yang diinginkan

# Memanggil fungsi untuk mencetak pola
cetak_pola(baris)


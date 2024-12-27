# Fungsi untuk penjumlahan
def tambah(a, b):
    return a + b

# Fungsi untuk pengurangan
def kurang(a, b):
    return a - b

# Fungsi untuk perkalian
def kali(a, b):
    return a * b

# Fungsi untuk pembagian
def bagi(a, b):
    if b == 0:
        return "Error! Pembagian dengan nol tidak diperbolehkan."
    else:
        return a / b

# Masukkan input langsung di bawah ini:
pilihan = '1'  # Pilihan operasi (1: penjumlahan, 2: pengurangan, 3: perkalian, 4: pembagian)
angka1 = 15  # Angka pertama
angka2 = 5   # Angka kedua

# Memanggil fungsi yang sesuai berdasarkan pilihan pengguna
if pilihan == '1':
    hasil = tambah(angka1, angka2)
    print(f"Hasil: {angka1} + {angka2} = {hasil}")
elif pilihan == '2':
    hasil = kurang(angka1, angka2)
    print(f"Hasil: {angka1} - {angka2} = {hasil}")
elif pilihan == '3':
    hasil = kali(angka1, angka2)
    print(f"Hasil: {angka1} * {angka2} = {hasil}")
elif pilihan == '4':
    hasil = bagi(angka1, angka2)
    print(f"Hasil: {angka1} / {angka2} = {hasil}")
else:
    print("Pilihan tidak valid! Silakan pilih 1, 2, 3, atau 4.")

def hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja):
    total_gaji = 0  # Menyimpan total gaji bulanan
    
    for jam_kerja in jam_kerja_per_hari:
        if jam_kerja > 8:
            # Menghitung lembur
            jam_lembur = jam_kerja - 8
            gaji_harian = (8 * tarif_per_jam) + (jam_lembur * tarif_per_jam * 1.5)
        else:
            # Tidak ada lembur
            gaji_harian = jam_kerja * tarif_per_jam
        
        total_gaji += gaji_harian
    
    return total_gaji

# Masukkan input langsung di bawah ini:
tarif_per_jam = 50000  # Gaji per jam
hari_kerja = 5  # Jumlah hari kerja dalam sebulan
jam_kerja_per_hari = [9, 8, 7, 10, 8]  # Jam kerja per hari

# Menghitung total gaji bulanan
total_gaji = hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja)

# Menampilkan total gaji bulanan
print(f"Total gaji bulanan: {total_gaji:.2f}")

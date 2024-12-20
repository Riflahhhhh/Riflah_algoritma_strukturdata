# variabel global untuk menyimpan data buku
buku = []
#fungsi untuk menampilkan semua data
def show_data():
    if len(buku) <= 0:
        print("BELUM ADA DATA")
    else:
        for indeks in range(len(buku)):
            print(f"[{indeks}] {buku[indeks]}")

#fungsi untuk menambah data
def insert_data():
    buku_baru = input("judul buku: ")
    buku.append(buku_baru)

#fungsi untuk edit data
def edit_data():
    show_data()
    indeks = int(input("inputkan ID buku: "))
    if indeks > len(buku):
        print("ID salah")
    else:
        judul_baru = input("judul baru: ")
        buku[indeks] = judul_baru

#fungsi untuk menghapus data
def delete_data():
    show_data()
    indeks = int(input("inputkan ID buku: "))
    if indeks > len(buku):
        print("ID salah")
    else:
        buku.remove(buku[indeks])

#fungsi untuk menampilkan menu
def show_menu():
    print("\n")
    print("----------- MENU -----------")
    print("[1] show data")
    print("[2] insert data")
    print("[3] edit data")
    print("[4] delete data")
    print("[5] exit")

    menu = input("PILIH MENU> ")
    print("\n")

    if int(menu) == 1:
        show_data()
    elif int(menu) == 2:
        insert_data()
    elif int(menu) == 3:
        edit_data()
    elif int(menu) == 4:
        delete_data()
    elif int(menu) == 5:
        print("keluar dari program.")
        exit()
    else:
        print("pilihan tidak valid, silahkan coba lagi")


    if __name__ == "__main__":
        while True:
            show_menu()

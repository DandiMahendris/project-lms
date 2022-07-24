# Untuk membuat Database dan Table Library
import buatTable

# Untuk fungsi pilihan Tugas
import inputData

finished = False;  # Boolean False

# Membuat program pilihan dengan finished bernilai False, maka apabila boolean yang diterima TRUE (not False)
# program akan terus berjalan

while not finished:
    
    # Membuat Tampilan menu awal bagi user untuk memilih tugas yang hendak dilakukan
    
    lib_manajemen = """
    ---------LIBRARY MANAGEMENT------------

        1. Pendaftaran User Baru
        2. Pendaftaran Buku Baru
        3. Peminjaman
        4. Tampilkan Daftar User
        5. Tampilkan Daftar Buku
        6. Tampilkan Daftar Peminjam
        7. Cari Buku
        8. Pengembalian
        9. Keluar
    
    ---------------------------------------
    """
    
    print(lib_manajemen);  # Menampilkan Menu
    
    pilihan = int(input("Masukkan Nomor Tugas: "))  # Melakukan input pilihan tugas
    
    if pilihan == 1:
        inputData.input_user()  # Input data user

    elif pilihan == 2:
        inputData.input_buku()  # Input data buku yang akan di stock
        
    elif pilihan == 3:
        inputData.input_peminjam()  # Input data untuk peminjam
        
    elif pilihan == 4:
        inputData.daftar_user()  # Input menampilkan daftar user
        
    elif pilihan == 5:
        inputData.daftar_buku()  # Input menampilkan daftar buku tersedia
        
    elif pilihan == 6:
        inputData.daftar_peminjam  # Input menampilkan daftar peminjam
        
    elif pilihan == 7:  # Input untuk mencari buku
        inputData.cari_buku()
        
    elif pilihan == 8:  # Input untuk pengembalian buku
        inputData.pengembalian()
        
    elif pilihan == 9:  # Input untuk keluar dari program
        print("""
        --------------------------
        Hope you enjoy our feature
        Thank you!
        -----------
        """)
        finished = True;
    
    else:  
        print("""
        --------------------------
        Incorrect Input Value
        -----------
        """)

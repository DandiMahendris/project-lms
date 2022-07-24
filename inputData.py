# Fungsi Tugas

from datetime import datetime  # Import module datetime
from datetime import timedelta # Import module dateime untuk penambahan hari

import ConnectSQL  # Import module ConnectSQL

# Params
user = 'root'
pw = "Megalumeng123"
host = "localhost"
db = "project_library"


connection = ConnectSQL.create_server_connection(host, user, pw)
    
connection = ConnectSQL.create_db_connection(host_name=host, user_name=user, user_password=pw, db_name=db)


def input_user():
    """Fungsi untuk input data user.
    
    Parameter input
    ----------
    nama_user, tgl_lahir, pekerjaan, alamat
    
    Query
    -----------
    (INSERT INTO .. ( .., ..) VALUES(%s, %s), var)
    
    var = variable untuk ditambahkan kedalam query sql.
    type(var) = <tuple>
    
    Melakukan eksekusi query 
    ConnectSQL.execute_query_var
    
    """
    nama_user = str(input("Masukkan nama user:  "))
    tgl_lahir = str(input("Masukkan tanggal lahir(YYYY-MM-DD):  "))
    pekerjaan = str(input("Masukkan nama pekerjaan:  "))
    alamat = str(input("Masukkan alamat:  "))


    query_input_user = """
    INSERT INTO daftar_user(nama_user, tanggal_lahir, pekerjaan, alamat) 
    VALUES(%s,%s,%s,%s);""" 

    var_user = (nama_user, tgl_lahir, pekerjaan, alamat)
        
    ConnectSQL.execute_query_var(connection, query_input_user, var_user)

    print(f"user {nama_user} telah berhasil ditambahkan")

    
def input_buku():
    """Fungsi untuk input data buku.
    
    Parameter input
    ----------
    id_buku, nama_buku, kategori, stok_buku
    
    Query
    -----------
    (INSERT INTO .. ( .., ..) VALUES(%s, %s), var)
    
    var = variable untuk ditambahkan kedalam query sql 
    type(var) = <tuple>
    
    Melakukan eksekusi query dengan,
    ConnectSQL.execute_query_var
    
    """
    kode_buku = str(input("Masukkan kode buku:  "))
    nama_buku = str(input("Masukkan nama buku:  "))
    kategori = str(input("Masukkan kategori:  "))
    stock = str(input("Masukkan stok buku:  "))
                    
    query_input_buku = """
    INSERT INTO daftar_buku(id_buku, nama_buku, kategori_buku, stok_buku) 
    VALUES(%s,%s,%s,%s);""" 

    var_buku = (kode_buku, nama_buku, kategori, stock)
        
    ConnectSQL.execute_query_var(connection, query_input_buku, var_buku)

    print(f"Buku {nama_buku} telah di tambahkan dalam kategori {kategori}")

    
def input_peminjam():
    """Fungsi untuk input data peminjam.
    
    Parameter input
    ----------
    id_user, id_buku, nama_peminjam, nama_buku, tgl_pinjam
    
    Query
    -----------
    (INSERT INTO .. ( .., ..) VALUES(%s, %s), var)
    
    var = variable untuk ditambahkan kedalam query sql 
    type(var) = <tuple>
    
    Melakukan eksekusi query dengan,
    ConnectSQL.execute_query_var
    """
    
    id_user = str(input("Masukkan id user:  "))
    nama_peminjam = str(input("Masukkan nama peminjam:  "))
    kode_buku = str(input("Masukkan kode buku:  "))
    nama_buku = str(input("Masukkan nama buku:  "))
    tgl_pinjam = str(input("Masukkan tanggal peminjaman:  "))

    yy, mm, dd = [int(x) for x in tgl_pinjam.split('-')]
    tgl_pengembalian = (datetime(yy, mm, dd) + timedelta(days=3)).strftime('%Y-%m-%d')
                                                                  
    query_pinjam_buku = """
    INSERT INTO peminjam(id_user, id_buku, nama_user, nama_buku, tanggal_pinjam, tanggal_pengembalian) 
    VALUES(%s,%s,%s,%s,%s,%s);""" 

    var_pinjam = (id_user, kode_buku, nama_peminjam, nama_buku, tgl_pinjam, tgl_pengembalian)
        
    ConnectSQL.execute_query_var(connection, query_pinjam_buku, var_pinjam)

    print(f"Peminjam {nama_peminjam} telah ditambahkan")

    
def daftar_user():
    """Fungsi untuk menampilkan table daftar user.
    
    Query
    -----------
    (SELECT .. FROM ... )
    
    Melakukan eksekusi query dengan,
    ConnectSQL.read_query
    """
    
    query = """
    SELECT * FROM daftar_user;
    """

    table_user = ConnectSQL.read_query(connection, query)

    print(table_user)
    

def daftar_buku():
    """Fungsi untuk menampilkan table daftar buku.
    
    Query
    -----------
    (SELECT .. FROM ... )
    
    Melakukan eksekusi query dengan,
    ConnectSQL.read_query
    """
    
    query = """
    SELECT * FROM daftar_buku;
    """
        
    table_buku = ConnectSQL.read_query(connection, query)

    print(table_buku)

    
def daftar_peminjam():
    """Fungsi untuk menampilkan table daftar peminjam.
    
    Query
    -----------
    (SELECT .. FROM ... )
    
    Melakukan eksekusi query dengan,
    ConnectSQL.read_query
    """
    
    query = """
    SELECT * FROM peminjam;
    """

    table_peminjam = ConnectSQL.read_query(connection, query)  

    print(table_peminjam)

    
def cari_buku():
    nama_buku = str(input('Masukkan nama buku:  '))

    query = """
    SELECT * FROM daftar_buku WHERE nama_buku = %s;
    """
    var_pinjam = (nama_buku,)

    table_buku = ConnectSQL.read_query_pencarian(connection, query, var_pinjam)

    print(table_buku)

    
def pengembalian():
    id_user = str(input('Masukkan id peminjam:  '))
    id_buku = str(input('Masukkan id buku:  '))

    query = """
    DELETE FROM peminjam WHERE id_user = %s and id_buku = %s;
    """
    var_pengembalian = (id_user, id_buku)

    ConnectSQL.execute_query_var(connection, query, var_pengembalian)

    print('Buku sudah dikembalikan')
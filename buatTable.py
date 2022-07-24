## Module untuk Membuat Table

import ConnectSQL  # Import module ConnectSQL

# Parameter
user = 'root'
pw = "Megalumeng123"
host = "localhost"
db = "project_library"

# Melakukan koneksi ke server
connection = ConnectSQL.create_server_connection(host, user, pw)

# Membuat database untuk program yang akan di jalankan
create_database_query = "CREATE DATABASE project_library"
ConnectSQL.create_database(connection, create_database_query) # Melakukan eksekusi sql query

# Melakukan koneksi ke database
connection = ConnectSQL.create_db_connection(host_name=host, user_name=user, user_password=pw, db_name=db)

# Memilih database yang akan digunakan
query_use_database = """
USE project_library;
"""
ConnectSQL.execute_query(connection, query_use_database)


# Membuat table daftar user untuk peminjaman buku
query_table_daftar_user = """
CREATE TABLE daftar_user(
	id_user INT NOT NULL AUTO_INCREMENT,
    nama_user VARCHAR(50),
    tanggal_lahir DATE,
    pekerjaan VARCHAR(30),
    alamat VARCHAR(50),
    PRIMARY KEY (id_user)
);
"""

# Melakukan eksekusi query untuk membuat table daftar user
ConnectSQL.execute_query(connection, query_table_daftar_user)

# Membuat table daftar buku yang ada
query_table_daftar_buku = """
CREATE TABLE daftar_buku(
	id_buku INT PRIMARY KEY,
    nama_buku INT,
	kategori_buku VARCHAR(30),
    stok_buku INT 
);
"""

# Melakukan eksekusi query untuk membuat table daftar buku
ConnectSQL.execute_query(connection, query_table_daftar_buku)

# Membuat table daftar peminjaman buku
query_table_peminjam = """
CREATE TABLE peminjam(
	id_user INT,
    id_buku INT,
    nama_user VARCHAR(50),
    nama_buku VARCHAR(50),
    tanggal_pinjam DATE,
    FOREIGN KEY (id_user) REFERENCES daftar_user(id_user) ON UPDATE CASCADE,
    FOREIGN KEY (id_buku) REFERENCES daftar_buku(id_buku) ON UPDATE CASCADE
);
"""

# Melakukan eksekusi query untuk membuat table daftar peminjam
ConnectSQL.execute_query(connection, query_table_peminjam)


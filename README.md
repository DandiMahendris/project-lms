<!-- Table of Content -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- About The Project -->
## About the Project
### Library Management System for Digital Book Library

### Username / discourseID
#### dandi-p4Gx

### Learning Objective
* Membuat program LMS menggunakan Python
* Membuat program python yang dapat terhubung ke database relational
* Mengaplikasikan pembuatan program dengan paradigma pemrograman berbasis fungsi atau pemrograman berbasis objek
* Mengaplikasikan penulisan kode yang bersih (mengacu ke PEP 8)


## Built With
* python 3.6 
* MySQL
* pandas
* datetime
* mysql module

<!--Getting Started-->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.

## Prerequisites
* This Project using 4 local module:
  - ConnectSQL.py
  - buatTable.py
  - inputData.py
  - main.py
* Make sure your system installed python 3.6 or more already
* Make sure MySQL installed already

### ConnecSQL.py Modul
Module untuk menghubungkan python dengan database dan membaca query sql.

Melakukan import mysql.connector
melakukan import pandas

1. Membuat fungsi yang akan digunakan untuk melakukan koneksi ke Server.
`create_server_connection(host_name, user_name, user_password)`

2. Fungsi membuat database
`create_database(connection, query)`

3. Fungsi untuk koneksi ke database
`create_db_connection(host_name, user_name, user_password, db_name)`

4. Fungsi untuk mengeksekusi query MySQL seperti Create, Update, Modify dan Delete Table
`execute_query(connection, query)`

5. Fungsi untuk mengeksekusi query MySQL dengan variabel python
`execute_query_var(connection, query, var)`

6. Fungsi untuk mengeksekusi query untuk penyajian dan filtering table
`read_query(connection, query)`

7. Fungsi untuk mengeksekusi query penyajian dan filtering table dengan input variable python
`read_query_pencarian(connection, query, var)`

### buatTable.py module
Module untuk membuat table yang diperlukan dalam library buku digital.

1. Melakukan import module ConnectSQL yang sudah dideksripsikan sebelumnya
`import ConnectSQL`

2. Melakukan koneksi ke Server dengan host_name, user_name, password
`ConnectSQL.create_server_connection(host, user, pw)`

3. Membuat Database bernama project_library
`create_database_query = "CREATE DATABASE project_library"`

4. Melakukan koneksi ke Database

5. Memilih database project_library tersebut

6. Membuat table daftar_user

7. Membuat table daftar_buku

8. Membuat table peminjam 





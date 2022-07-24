## Module untuk menghubungkan python dengan database dan membaca query sql

import mysql.connector  # Import library untuk menghubungkan mysql dengan python
from mysql.connector import Error
import pandas as pd  # import pandas untuk menampilkan table dari database mysql


def create_server_connection(host_name, user_name, user_password):
    """ Fungsi untuk koneksi ke server.

    Parameters
    ----------
    host_name : nama host sql
    user_name : nama user sql
    user_password : password sql
    """
    connection = None
    
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        print("MySQL connection successful")
    except Error as err:
        print("Error: {}".format(err))

    return connection


def create_database(connection, query):
    """ Fungsi untuk membuat database.
    
    Parameters
    ----------
    connection : create_server_connection(host, user, pw)
    query : query mysql untuk membuat database
    
    (CREATE DATABASE ...)
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print("Error: {}".format(err))


def create_db_connection(host_name, user_name, user_password, db_name):
    """ Fungsi koneksi ke database.
    
    Parameters
    ----------
    host_name : nama host sql
    user_name : nama user sql
    user_password : password sql
    db_name : nama database
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name)
        print("MySQL database connection successfull")
    except Error as err:
        print("Error: {}".format(err))
    return connection
        

def execute_query(connection, query):
    """ Fungsi untuk Eksekusi Query, Create, Update, Modify dan Delete data
    
    Parameters
    ----------
    connection : koneksi ke database
    query : query mysql untuk editing data
    
    (INSERT INTO ...(...) VALUES(...))
    (ALTER TABLE ... ADD / MODIFY / DROP / SET / ...)
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query berhasil dieksekusi")
    except Error as err:
        print("Error: {}".format(err))
        
# Fungsi untuk eksekusi query dengan input Variable
def execute_query_var(connection, query, var):
    """ Fungsi untuk eksekusi Query create, update, delete data dengan variable.
    
    Fungsi digunakan dengan tiga parameter, hal ini bertujuan untuk dapat melakukan 
    input variable yang di buat dengan python ke dalam sql query (Umum nya variable 
    menggantikan %s pada query sql.)

    Parameters
    ----------
    connection : koneksi ke database.
    query : query mysql dengan parameter %s sebagai variable yang akan di input.
    var : variable yang di tentukan. type <tuple>, <list>, <dict>
          
    ((INSERT INTO ...(...) VALUES(%s, %s, ... )), var)

    Caution, gunakan input var* dengan type yang sudah ditentukan, selain type tersebut
    akan menghasilkan error.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, var)
        connection.commit()
        print("Query berhasil dieksekusi")
    except Error as err:
        print("Error: {}".format(err))


def read_query(connection, query):
    """ Fungsi query untuk melakukan Penyajian dan Filtering Table dari database.
    
    Parameters
    ----------
    connection : koneksi ke database.
    query : query mysql untuk filtering dan penyajian table.
    
    (SELECT ... FROM ...)
    """
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        return pd.DataFrame(result, columns=[field_names])
    except Error as err:
        print("Error: {}".format(err))


def read_query_pencarian(connection, query, var):
    """ Fungsi query untuk melakukan penyajian dan filtering dengan variable.
    
    Parameters
    ----------
    connection : koneksi ke database.
    query : query mysql dengan parameter %s sebagai variable yang akan di input.
    var : variable yang di tentukan. type <tuple>, <list>, <dict>
    
    ((SELECT ... FROM ... WHERE ... %s), var)
    """
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query, var)
        result = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        return pd.DataFrame(result, columns=[field_names])
    except Error as err:
        print("Error: {}".format(err))

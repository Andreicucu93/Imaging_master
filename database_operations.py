import pyodbc

#Database connection START
conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Space\\Database\\MC_Productlibrary.accdb;'
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("SELECT ID, Desc20, Name FROM MC_Products")
#Database connection END
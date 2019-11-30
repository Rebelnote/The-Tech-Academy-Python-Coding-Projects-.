import sqlite3

conn = sqlite3.connect('fileType.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileID( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('fileType.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_fileID(col_fileName) VALUES (?)", \
                ['information.docx'])
    cur.execute("INSERT INTO tbl_fileID(col_fileName) VALUES (?)", \
                ['Hello.txt'])
    cur.execute("INSERT INTO tbl_fileID(col_fileName) VALUES (?)", \
                ['myImage.pnp'])
    cur.execute("INSERT INTO tbl_fileID(col_fileName) VALUES (?)", \
                ['myMovie.mpg'])
    cur.execute("INSERT INTO tbl_fileID(col_fileName) VALUES (?)", \
                ['World.txt'])
    cur.execute("INSERT INTO tbl_fileID(col_fileName) VALUES (?)", \
                ['data.pdf'])
    cur.execute("INSERT INTO tbl_fileID(col_fileName) VALUES (?)", \
                ['myPhoto.jpg'])
    conn.commit()
conn.close()

conn = sqlite3.connect("fileType.db")

with conn:
    cur = conn.cursor()
    cur.execute("SELECT ALL col_fileName FROM tbl_fileID WHERE col_fileName LIKE '%txt'")
    varText = cur.fetchall()
    for item in varText:
        msg = "File Name: {}".format(item[])
    print(msg)

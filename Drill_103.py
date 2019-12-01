import sqlite3


conn = sqlite3.connect('Drill_103.db')

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID  INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileNames TEXT \
        )")

for fileNames in fileList:
    if fileNames.endswith(".txt"):
        cur.execute("INSERT INTO tbl_files(col_FileNames) VALUES (?)", (fileNames,))
    
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_FileNames FROM tbl_files")
    printFiles = cur.fetchall()
    print(printFiles)
    conn.commit()
conn.close()











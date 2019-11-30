
import os

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')


def txtFiles():
    for filename in fileList:
        if filename.endswith('txt'):
            print(os.path.join("fileList", filename))
            continue
        else:
            continue

if __name__ == "__main__": 
    txtFiles()

import os

fPath = "/Users/matthewedey/Documents/Test_Drill"

listOne = os.listdir(fPath)
fileTime = os.path.getmtime(fPath)


def txtFiles():
    for filename in listOne:
        if filename.endswith('txt'):
            print(os.path.join("fPath", filename))
            print(fileTime)
            continue
        else:
            continue

if __name__ == "__main__": 
    txtFiles()











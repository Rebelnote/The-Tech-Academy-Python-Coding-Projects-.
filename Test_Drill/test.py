import os

fPath = "Users/matthewedey/Documents/Drill_100"

listOne = os.listdir(fPath)


def txtFiles():
    for filename in listOne:
        if filename.endswith('txt'):
            print(os.path.join("fPath", filename))
            continue
        else:
            continue

if __name__ == "__main__": 
    txtFiles()











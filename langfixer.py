
import wget
import os
print("Importing packages")

debug = True


print("Downloading page")
url = "https://raw.githubusercontent.com/BenBUnity/lang/main/words" 
data = wget.download(url, 'data2.txt')
print(data)
print("Data parsing")
f = open(data, 'r')
impWords = f.read().split("\n")
words = []

for i in impWords:
        if i != "":
            words.append(i.split(","))
            if debug:
                print(i.split(","))


print("Data parsed")




while True:
    
    print("SenseiLangTM - Kode Ninjas language fixer")
    epocWord = input("Word input? > ")

    done = epocWord.translate(str.maketrans('ck', 'kc'))
    done = done.translate(str.maketrans('CK', 'KC'))
    
    for fixIt in words:
        done = done.replace(fixIt[0],fixIt[1])

    

    input(done + "\n\n")

localVer = 2


import wget
import os
print("Importing pakcages")

debug = False\


print("Getting ready")
url = "https://raw.githubusercontent.com/BenBUnity/lang/main/verCheck" 
verCheck = wget.download(url, 'verCheck.txt')
verCheckData = open(verCheck, 'r').read()
os.remove(verCheck)

if int(verCheckData) > localVer:
    input("\n------\n\nA newer version of this program is available (v" + str(int(verCheckData)) + ")\n\n[Enter] Kontinue\n\n------\n")


print("Downloading page")
url = "https://raw.githubusercontent.com/BenBUnity/lang/main/words" 
data = wget.download(url, 'words.txt')
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

os.remove(data)
print("Data parsed")



while True:
    
    print("\n\nSenseiLangTM - Kode Ninjas language fixer")
    epocWord = input("\nInput > ")

    done = epocWord.translate(str.maketrans('ck', 'kc'))
    done = done.translate(str.maketrans('CK', 'KC'))
    
    for fixIt in words:
        done = done.replace(fixIt[0],fixIt[1])

    
    print("Output v")
    input(done + "\n\n[Enter] Start again\n\n------")

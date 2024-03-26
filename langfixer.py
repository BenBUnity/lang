localVer = 3


import wget
import os
print("Importing pakcages")

debug = False\

def checkUpdate():
    print("Getting ready")
    url = "https://raw.githubusercontent.com/BenBUnity/lang/main/verCheck" 
    verCheck = wget.download(url, 'verCheck.txt')
    verCheckData = open(verCheck, 'r').read()
    os.remove(verCheck)

    if int(verCheckData) > localVer:
        input("\n------\n\nA newer version of this program is available (v" + str(int(verCheckData)) + ")\n\n[Enter] Kontinue\n\n------\n")


def parseWords():
    print("Downloading page")
    url = "https://raw.githubusercontent.com/BenBUnity/lang/main/words" 
    data = wget.download(url, 'words.txt')
    print(data)
    print("Data parsing")
    f = open(data, 'r')
    impWords = f.read().split("\n")
    global words
    words = []
    
    for i in impWords:
            if i != "":
                words.append(i.split(","))
                if debug:
                    print(i.split(","))

    os.remove(data)
    print("Data parsed\n\n------")

def main():
    while True:
        
        print("\n\nSenseiLangTM - Kode Ninjas language fixer\n[E] Exit - [R] Refresh Diktionary")
        konvert = input("\nInput > ")
        
        if konvert == "E":
            return
        elif konvert == "R":
            parseWords()
        else:
            done = konvert.translate(str.maketrans('ck', 'kc'))
            done = done.translate(str.maketrans('CK', 'KC'))
            
            for fixIt in words:
                done = done.replace(fixIt[0],fixIt[1])

            
            print("Output v\n")
            input(done + "\n\n[Enter] Start again\n\n------")


checkUpdate()
parseWords()
main()



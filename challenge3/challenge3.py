import re

def decryptData():
    pattern = "[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}"

    with open("code.txt", 'r') as f:
        matched = re.findall(pattern, f.read())
        word = []
        for matchedStr in matched :
            word.append(matchedStr[4])
        print(''.join(word))

decryptData()
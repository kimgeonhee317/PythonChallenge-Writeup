
import re

def decryptData():
    target = []
    pattern = "[A-Za-z0-9]"
    
    with open("code.txt", 'r') as f:
        for char in f.read():
            if (re.match(pattern, char)):
                target.append(char)
            else:
                continue
    print(''.join(target))
            
decryptData()
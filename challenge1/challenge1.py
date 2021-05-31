import re

def translate():
    #source = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    source = "map"
    target = []
    pattern1 = "[a-x]"
    pattern2 = "[y-z]"
    for char in source:
        if (re.match(pattern1, char)):
            target.append(chr(ord(char)+2))
        elif (re.match(pattern2, char)):
            target.append(chr(ord(char)-24))
        else:
            target.append(char)
            
    print(''.join(target))

translate()
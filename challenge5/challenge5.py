import pickle

def loadPickle(filePath):
    with open(filePath, 'rb') as f:
        data = pickle.load(f)
        #print(data)    
    return data

def decryptData(char, number):
    dataStr = ""
    if char==" ":
        dataStr = "_"*number
    else :
        dataStr = "#"*number
    return dataStr

def main():
    mainStr =[]
    encryptedData = loadPickle("code.txt")
    for dataArray in encryptedData:
        for dataTuple in dataArray:
             dataList = list(dataTuple)
             mainStr.append(decryptData(dataList[0], dataList[1]))
    binaryStr = "".join(mainStr)

    byteNum = 95
    for i in range(0, len(binaryStr), byteNum):
        print(binaryStr[i:i+byteNum])
        
main()
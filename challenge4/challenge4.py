import requests
import re
def getHttpData():
    
    parameter = 12345
    for i in range(0,400):
        URL = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={parameter}'    
        r = requests.get(URL)
        number = re.findall("[0-9]+", r.text) 
        if len(number) == 0:
            print(i, r.text)
            parameter /= 2        
        else:
            print(i, r.text)
            parameter = int(''.join(number))
            if(parameter == 8268363579):
                parameter = 63579
        if re.match("[\w]*[.]html", r.text):
            print(r.text)
            break

getHttpData()

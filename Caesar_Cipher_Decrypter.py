data = input("Enter the string you want to decrypt:")
key = int(input("Enter the key: "))
chars = list(data)
if(key > 25):
    print("Key out of range.")
else:
    outerarray = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    innerarray = list(outerarray)
    i = 0
    while(i!=26):
        innerarray[i] = outerarray[(i+key)%26]
        i = i+1
    sentence = ''
    for c in chars:
        if (c == ' '):
            decrypt = ' '
            sentence = sentence + decrypt
        else:
            j = 0
            while(j!=26):
                if(innerarray[j].lower() == c.lower()):
                    position = j
                    decrypt = outerarray[j]
                    sentence = sentence + decrypt
                    break
                j = j+1
    print(sentence)
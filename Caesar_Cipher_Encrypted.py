data = input("Enter the string you want to encrypt:")
key = int(input("Enter the shift key:"))
if (key > 25):
    print("Key value out of range.")
else:
    outerarray = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    innerarray = list(outerarray)
    chars = list(data)
    i = 0
    while(i!=26):
        innerarray[i] = outerarray[(i+key)%26]
        i = i+1
    sentence = ''
    for c in chars:
        if (c == ' '):
            encrypt = ' '
            sentence = sentence + encrypt
        else:
            j = 0
            while(j!=26):
                if(outerarray[j].lower() == c.lower()):
                    position = j
                    encrypt = innerarray[position]
                    sentence = sentence + encrypt
                    break
                j = j+1
    print(sentence)

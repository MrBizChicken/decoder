import random
def decoder(num):
    text = input("enter text to decode")
    result = ""
    for t in text:
        result += chr(ord(t) - num)

    print(num, ":", result)


decoder(5)

def encoder():
    text = input(("enter text to encript"))
    offset = 5
    string = ""
    for t in text:
        o = ord(t)
        c = chr(o + offset)

        string += c
    print(string)


encoder()

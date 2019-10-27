def simplify_text(s):
    newS = ''
    spclChar = ["-","'"," "]
    for c in s:
        if c.isupper() and c.isalpha():
            c = chr(ord(c)+32)
        elif c not in spclChar and not c.isalpha():
            c = ''
        newS += c
         
    print(newS)

userInput = input('Enter string : ')
simplify_text(userInput)

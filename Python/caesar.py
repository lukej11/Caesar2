#This is a tutorial from the book Invent Your
#Own Computer Games with Python

#Caesar cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS) #establishing a constant size of 1 and 52

def getMode():#defining a function that finds out if the user wants to encrypt or decrypt the message
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']: #using an if statement to determine whether the user wants to encrypt or decrypt a particular message
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    print('Enter your message: ') # similiar to a get_int() variable in C. It is recieving input from the user and  storing the information
    return input()

def getKey():
    key = 0 #creates variable and initializes it
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE)) #asks user for key
        key = int(input()) #forces key given to integer format
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: #Symbol not found in SYMBOLS
            #Just add this symbol without any change
            translated += symbol
        else:
            #Encrypt or decrypt
            symbolIndex += key
        if symbolIndex >= len(SYMBOLS):#the shirtgs tat happening here depending on the length of SYMBOl list and the key
            symbolIndex -= len(SYMBOLS)
        elif symbolIndex < 0:
            symbolIndex += len(SYMBOLS)

        translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode()#these are the call functions
message = getMessage()
key = getKey()
print('Your translated text is: ')#print statements
print(getTranslatedMessage(mode, message, key))#print statements

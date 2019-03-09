char = input("Plase enter your alphabet to check ")
if (ord(char)>=65 and ord(char)<=90):
    print("You have entered an upper case alphabet")
    if (char in ['A','E','I','O','U']):
        print("You have entered an upper case Vowel Alphabet")
    else:
        print("You have entered a consonent")
elif (ord(char)>=97 and ord(char)<=122):
        print("You have entered a lower case alphabet")
        if(char in ['a','e','i','o','u']):
           print("You have entered a lower case vowel alphabet")
        else:
           print:("You have entered a consonent")
else:
    print("This is not an alphabet")
           

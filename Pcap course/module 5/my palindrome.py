mystring=input("input a string: ")
mystring=mystring.replace(" ",'')
mystring=mystring.upper()
ln=len(mystring)-1

def palindrome(string):
    pal=True
    for char in mystring:
        poz=mystring.index(char)
        if char != mystring[poz-ln]:
            pal=False
        if pal==False:
            return("it is not a palindrome")
        else:
            return("it is indeed a palindrome")


print(palindrome(mystring))
import string

text_to_encrypt=input("just put a string bastard: ")

""" only activate when you don't want the whitespaces """
#text_to_encrypt= text_to_encrypt.replace(" ","")

e_k=int(input("input a encryption key from 1 to 25: "))
e_k=e_k%26


alph=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
Alph=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
chif=''
shifted1=alph[e_k:]+alph[:e_k]
shifted=Alph[e_k:]+Alph[:e_k]
for char in text_to_encrypt:
    if not char.isalpha() and char!=" ":
        continue
    elif char in alph:
        i=alph.index(char)
        chif+=shifted1[i]
    elif char in Alph:
        i=Alph.index(char)
        chif+=shifted[i]
    elif char is " ":
        chif+=" " 

""" only activate when  your string does not have special chars"""
#if len(chif)>=len(text_to_encrypt): 
print (chif)

""" ©Adelin 2021 """
""" for next level check v2.0 """
import string
def caesar(string,shift,alphabets):

    def shifted_alph(alphabets):
        return alphabets[shift:]+alphabets[:shift]
    shifted_alphabets=tuple(map(shifted_alph,alphabets))
    final_alphabets=''.join(alphabets)
    final_shifted=''.join(shifted_alphabets)
    translation_table=str.maketrans(final_alphabets,final_shifted)
    return text_to_encrypt.translate(translation_table)

text_to_encrypt=input("just put a string bastard: ")

""" only activate when you don't want the whitespaces """
#text_to_encrypt= text_to_encrypt.replace(" ","")

e_k=int(input("input a encryption key from 1 to 25: "))
e_k=e_k%26

print(caesar(text_to_encrypt,e_k,[string.ascii_lowercase,string.ascii_uppercase,string.punctuation]))

decrypt=input("do you want decrypt the text? ")

if decrypt=="yes" or decrypt=="Yes" or decrypt =="da":
    print(text_to_encrypt)
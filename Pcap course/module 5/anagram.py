string1=input("tell me a word: ")
string1=string1.replace(" ",'')
string1=string1.upper()
string2=input("tell me an anagram: ")
string2=string2.replace(" ",'')
string2=string2.upper()
list1=[]
list2=[]
for char in string1:
    list1.append(char)
for char in string2:
    list2.append(char)
list1.sort()
list2.sort()
if list1==list2:
    print("Anagram")
else:
    print("this is not an anagram dummie")
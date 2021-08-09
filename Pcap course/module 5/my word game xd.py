string1=input("enter a word: ")
string2=input("enter a char string: ")
mylist=[]
num=''
t=True

for char in string1:
    if char in string2:
        num=''.join(str(string2.find(char)))
        
for char in range(len(num)-1):
    if num[char]>num[char+1]:
        t=False



if t==True and num[len(num)-1]>num[len(num)-2]:
    print('yes')
else:
    print('no')
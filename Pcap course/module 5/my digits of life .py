date=input("enter your birthday(DDMMYYYY): ")
mylist=[]
summ=0
if date.isdigit():
    for char in date:
        mylist.append(int(char))
else:
    print("it is not a valide date")
summ=sum(mylist)
while len(str(summ))>1:
    summ=sum(mylist)
    mylist=[]
    for char in str(summ):
        mylist.append(int(char))

print(summ)


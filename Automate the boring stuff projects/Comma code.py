k=[]
g=input("how much items do you want to type? ")

if g.isdigit():    
    
    for i in range(int(g)):
        k.append(input("tell me something: "))
    for elem in k[:-1]:
        print(elem,end=",")
    print("and "+k[-1])
    
    

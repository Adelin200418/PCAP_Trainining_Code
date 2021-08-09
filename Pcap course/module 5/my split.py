def mysplit(strng):
    if len(strng)>0:
    
    
        mylist=[]
        cuv=[]
        for i in strng:
            if i!=" ":
                cuv.append(i)
            elif i==" ":
                if cuv!=" ":
                    mylist.append("".join(cuv))
                    cuv=[]
                else:
                    cuv=[] 
        if cuv !="":
            mylist.append("".join(cuv))    
        for i in mylist:
            if i=='':
                mylist.remove('')

        if all('' == s or s.isspace() for s in mylist):
            return("[]")
        else:
           return(mylist) 
    else:
        return("[]")    



print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

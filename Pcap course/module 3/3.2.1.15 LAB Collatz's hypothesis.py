step=0
c0=int(input("c0 value is:"))
while c0!=1:
    if c0%2==0:
        c0=c0/2
        step=step+1
        print("\n c0 at step:",step,"is",c0)
    else:
        c0=c0*3+1
        step=step+1
        print("\n c0 at step:",step,"is",c0)
print("\n c0 at final step:",step," is ",c0)
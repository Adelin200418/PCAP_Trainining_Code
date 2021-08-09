beatles=[]
print("Step 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

for i in range (2):
    beatles.append(input("Names:"))
print("Step 3:", beatles)

del beatles[4]
del beatles[3]
print("Step 4:", beatles)

beatles.insert(0,"Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))

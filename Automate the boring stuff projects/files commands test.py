import os
#os.chdir('c:\\destop')
print(os.getcwd())

#os.makedirs('C:\destop\python\Automate the boring stuff projects\\new folder\ceva\\altceva')

print(os.path.relpath('Automate the boring stuff projects', 'c:\\'))

calcfilepath='C:\destop\python\Automate the boring stuff projects\The Collatz Sequence.py'
print(calcfilepath.split(os.path.sep))



#print(os.path.getsize('C:\destop\python\Automate the boring stuff projects\The Collatz Sequence.py'))
#print(os.listdir('C:\destop'))

""" totalSize=0
for filename in os.listdir('C:\\Windows\\System32'):
 totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize) """































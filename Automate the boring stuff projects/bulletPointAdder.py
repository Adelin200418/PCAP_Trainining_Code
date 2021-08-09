#! python3
# bulletPointAdder.py-adds bullet to wikipedia texts

import pyperclip
text=pyperclip.paste()

lines=text.split('\n')
for i in range(len(lines)):
    lines[i]='*'+ lines[i]
text='\n'.join(lines)

pyperclip.copy(text)
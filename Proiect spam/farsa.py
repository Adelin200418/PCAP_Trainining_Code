import pyautogui

print(pyautogui.position())
pyautogui.moveTo(584, 1036, 1)
pyautogui.click()
file = open("farsa.txt", "r", encoding="utf8")
for i in file:
    i = i.rstrip()
    if len(i) > 0:
        i = i.split()
        for j in i:
            pyautogui.write(str(j))
            pyautogui.press('enter')

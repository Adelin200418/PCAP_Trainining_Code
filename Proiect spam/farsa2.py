import pyautogui as pag
import pyperclip as pc

pag.moveTo(584, 1036, 1)
pag.click()
with open("farsa.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        pc.copy(line)
        pag.hotkey("ctrl", "v")
        pag.press("enter")

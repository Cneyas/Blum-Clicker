import pyautogui

hedef_goruntu = "image.png"

while True:
    positions = list(pyautogui.locateAllOnScreen(hedef_goruntu, confidence=0.9))

    if positions:
        for pos in positions:
            x, y = pos.left, pos.top
            pyautogui.click(x, y)
            print("+")
    else:
        print("Bulunamadı")
import pyautogui
from PIL import ImageGrab

x1, y1, x2, y2 = 100, 100, 500, 500

def main():
    global x1, y1, x2, y2

    key = input("start를 입력해주세요: ")
    if (key == "start"):
        x1, y1 = pyautogui.position()
        print(x1, y1)
    
    key = input("end를 입력해주세요: ")
    if (key == "end"):
        x2, y2 = pyautogui.position()
        print(x2, y2)

    count = 1
    
    while (True):
        key = input("캡처를 원하시면 c를 입력해주세요: ")
        if (key == "c"):
            capture(count)
            count += 1

def capture(count):
    screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    screenshot.save("screenshot%d.png" % count)

main()
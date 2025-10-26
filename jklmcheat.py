# jklm.cheat
import pyautogui
from pynput import mouse

with open("words1.txt", "r") as words:
    word_arr = [word.strip() for word in sorted(words)]

used_words = set()
typing_active = [False]  # flag to start typing
stop_flag = [False]      # flag to stop everything

def on_click(x, y, button, pressed):
    if pressed:
        if button == mouse.Button.left:
            typing_active[0] = True  # start typing
        if button == mouse.Button.right:
            stop_flag[0] = True      # stop everything
            return False

# start a global listener
listener = mouse.Listener(on_click=on_click)
listener.start()

while True:
    substr = input("substring> ")
    for word in word_arr:
        if stop_flag[0]:
            break
        if substr in word and word not in used_words and word.isalpha():
            # wait until left click has been pressed
            while not typing_active[0]:
                if stop_flag[0]:
                    break
            if stop_flag[0]:
                break

            pyautogui.write(word, interval=0.001)
            pyautogui.press("enter")
            used_words.add(word)


listener.stop()

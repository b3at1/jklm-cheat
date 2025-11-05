# jklm.cheat
# run with: chromium-browser -ozone-platform=x11
import pyautogui
from pynput import mouse

# load word list
with open("jlawer.txt", "r") as words:
    word_arr = sorted(w.strip() for w in words if w.strip())

used_words = set()

# flags (using lists so they’re mutable from inside listener)
typing_active = [False]
stop_flag = [False]

# mouse event handler
def on_click(x, y, button, pressed):
    if not pressed:
        return
    if button == mouse.Button.left:
        typing_active[0] = True           # start typing words
    elif button == mouse.Button.right:
        stop_flag[0] = True               # stop generating for current substring
        typing_active[0] = False          # reset typing state

# start the listener (don’t ever stop it)
listener = mouse.Listener(on_click=on_click)
listener.start()

while True:
    substr = input("substring> ").strip()
    if not substr:
        continue

    # reset flags for this round
    stop_flag[0] = False
    typing_active[0] = False

    for word in word_arr:
        if stop_flag[0]:
            break

        if substr in word and word not in used_words and word.isalpha():
            # wait until left-click pressed
            while not typing_active[0]:
                if stop_flag[0]:
                    break
            if stop_flag[0]:
                break

            pyautogui.write(word, interval=0.001)
            pyautogui.press("enter")
            used_words.add(word)

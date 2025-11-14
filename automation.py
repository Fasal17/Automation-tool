import time
import webbrowser
import pyautogui
import pygetwindow as gw


webbrowser.open("https://github.com")
print("Opened GitHub...")
time.sleep(5)

found = False
for title in gw.getAllTitles():
    if "github" in title.lower():
        win = gw.getWindowsWithTitle(title)[0]
        win.close()
        found = True
        print("Closed GitHub window.")
        break

if not found:
    print("Did not find GitHub window. Sending Alt+F4 instead.")
    pyautogui.hotkey('alt', 'f4')

time.sleep(1)
webbrowser.open("https://encryptbytes.com/")
print("Opened ERP.")
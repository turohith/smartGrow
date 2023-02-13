import tkinter as tk
from tkinter import ttk

versionNumber = 0.1
titleText = "smartGrow v"
window_width = 320
window_height = 240

#STRINGS AND THINGS
splashScreenText = f"SmartGrow v{versionNumber}"



root = tk.Tk()
root.title(f"{titleText}{versionNumber}")

#button function
def button_clicked():
    message.config(text='Button Pressed')

#get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#find center point
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)
root.overrideredirect(True)

message = ttk.Label(root)
message['text'] = f"{splashScreenText}"
message.pack()

button = ttk.Button(root, text='Click Me', command=button_clicked)
button.pack()

#mainLoop (keeps window running)
#needs to be the last statement, after creating widgets
root.mainloop()

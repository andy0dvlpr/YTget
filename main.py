import tkinter as tk
from tkinter import font

ytget_version = "3.0"

win = tk.Tk()
win.title("YTget " + ytget_version)
win.resizable(False, False)

def validateLink(*args):
    insertedLink = linkEntry.get()
    if insertedLink.startswith("https://www.youtube.com/watch?v="):
        validTextString.set("This is a valid link!")
        validLabel.config(fg="green")
    elif insertedLink.startswith("https://youtube.com/playlist?list="):
        validTextString.set("This is a playlist link! All videos will be downloaded sequentially.")
        validLabel.config(fg="green")
    else:
        validTextString.set("This doesn't seem to be a valid link.")
        validLabel.config(fg="red")

linkLabel = tk.Label(win, anchor="w", text="Link to video:")
linkVar = tk.StringVar()
linkEntry = tk.Entry(win, textvariable=linkVar, width=69) #nice
linkVar.trace("w", validateLink)

validTextString = tk.StringVar()
validLabel = tk.Label(win, textvariable=validTextString)
bold_font = font.Font(validLabel, validLabel.cget("font"))
bold_font.configure(weight="bold")
validLabel.config(font=bold_font)

linkLabel.grid(row=1, column=1)
linkEntry.grid(row=1, column=2)
validLabel.grid(row=2, column=1, columnspan=2, sticky="w")

win.mainloop()

import tkinter as tk
from tkinter import font
from tkinter import filedialog
from PIL import ImageTk, Image

ytget_version = "3.0"

win = tk.Tk()
win.title("YTget " + ytget_version)
win.resizable(False, False)
win.iconphoto(False, tk.PhotoImage(file = "images/icon-256p.png"))

# Display a message if the link is invalid, or is a playlist.
def validateLink(*args):
    insertedLink = linkEntry.get()
    if insertedLink.startswith("https://www.youtube.com/watch?v="):
        validTextString.set("")
    elif insertedLink.startswith("https://youtube.com/playlist?list="):
        validTextString.set("This is a playlist link! All videos will be downloaded sequentially.")
        validLabel.config(fg="green")
    else:
        validTextString.set("This doesn't seem to be a valid link.")
        validLabel.config(fg="red")

linkLabel = tk.Label(win, text="Link to video:")
linkVar = tk.StringVar()
linkEntry = tk.Entry(win, textvariable=linkVar, width=69) #nice
linkVar.trace("w", validateLink)
validTextString = tk.StringVar() # Used by validateLink(), which is called everytime the Entry is modified.
validLabel = tk.Label(win, textvariable=validTextString)
# Put a bold font on the text.
bold_font = font.Font(validLabel, validLabel.cget("font"))
bold_font.configure(weight="bold")
validLabel.config(font=bold_font)

formatFrame = tk.Frame(win)
formatLabel = tk.Label(formatFrame, text="Format:")
downloadFormat = tk.StringVar()
audioButton = tk.Radiobutton(formatFrame, text="Audio", variable=downloadFormat, value="audio")
audioButton.select() # We need to have a default option selected.
videoButton = tk.Radiobutton(formatFrame, text="Video", variable=downloadFormat, value="video")

DLFrame = tk.Frame(win)
DLLabel = tk.Label(DLFrame, text="Download location:")
DLOptions = ["Default location", "Choose another location..."]
DLSel = tk.StringVar()
DLSel.set(DLOptions[0])
def changeDL(*args):
    if DLSel.get() == DLOptions[1]:
        DLSel.set(filedialog.askdirectory())
        if not DLSel.get(): # If the user pressed "Cancel" on the folder selection dialog, revert back to default.
            DLSel.set(DLOptions[0])
downloadLocation = tk.OptionMenu(DLFrame, DLSel, *DLOptions, command=changeDL)
downloadLocation.config(width=30, anchor="w", padx=10, indicatoron=0)

## GEOMETRY ##

linkLabel.grid(row=1, column=1, sticky="w")
linkEntry.grid(row=2, column=1, columnspan=2)
validLabel.grid(row=3, column=1, columnspan=2, sticky="w")

formatFrame.grid(row=4, column=1, sticky="w")
# Part of formatFrame:
formatLabel.grid(row=1, column=1)
audioButton.grid(row=2, column=1, sticky="w")
videoButton.grid(row=3, column=1, sticky="w")

DLFrame.grid(row=4, column=2)
# Part of DLFrame:
DLLabel.grid(row=1, column=1)
downloadLocation.grid(row=2, column=1)

win.mainloop()

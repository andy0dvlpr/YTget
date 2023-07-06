import os
import json
import tkinter as tk
from tkinter import font
from tkinter import filedialog
from PIL import ImageTk, Image

ytget_version = "3.0"
ytget_optfolder = os.environ["APPDATA"] + "\\YTget"
if not os.path.exists(ytget_optfolder):
    os.makedirs(ytget_optfolder)
# Read settings:
try:
    optFile = open(ytget_optfolder + "\\settings", "r")
except FileNotFoundError:
    # The settings file does not exist, so initialize the settings blank.
    defaultDL = ""
else:
    # Load settings.
    locals().update(json.loads(optFile.read())) # Take the stored variables and load them.

win = tk.Tk()
win.title("YTget " + ytget_version)
win.resizable(False, False)
window_icon = tk.PhotoImage(file = "images/icon-256p.png")
win.iconphoto(False, window_icon)

def closeProgram():
    win.destroy()

def aboutWindowOpen():
# About window
    aboutwin = tk.Toplevel(win)
    aboutwin.title("About YTget")
    aboutwin.resizable(False, False)
    aboutwin.iconphoto(False, window_icon)

def optWindowOpen():
    optwin = tk.Toplevel(win)
    optwin.title("YTget Preferences")
    optwin.resizable(False, False)
    optwin.iconphoto(False, window_icon)

    optw = tk.Frame(optwin) # Frame for universal padding.
    opt_defaultDLLabel = tk.Label(optw, text="Default save location:")
    opt_defaultDL = tk.StringVar()
    if not defaultDL: # If the setting is blank, use default:
        opt_defaultDL.set(os.environ["USERPROFILE"] + "\\Downloads")
    else:
        opt_defaultDL.set(defaultDL)
    opt_defaultDLEntry = tk.Entry(optw, textvariable=opt_defaultDL, width=30)
    def opt_getDefaultDL():
        optwin.attributes("-topmost", 0) # Due to a tkinter bug, child windows go behind root windows when a file dialog opens.
        newDefaultDL = filedialog.askdirectory()
        optwin.attributes("-topmost", 1) # Now we set it back. This is how we circumvent the tkinter bug.
        if newDefaultDL: # If the user selected a folder
            opt_defaultDL.set(newDefaultDL)
    opt_defaultDLButton = tk.Button(optw, text="Choose location", command=opt_getDefaultDL)

    # OK and Cancel Buttons:
    def opt_SaveSettings():
        opt_Settings = {
            "defaultDL": opt_defaultDL.get()
        }
        jsonSettings = json.dumps(opt_Settings)
        optFile = open(ytget_optfolder + "\\settings", "w")
        optFile.write(jsonSettings)
        optFile.close()
    opt_ButtonFrame = tk.Frame(optw)
    opt_SaveButton = tk.Button(opt_ButtonFrame, text="OK", command=opt_SaveSettings)
    opt_CancelButton = tk.Button(opt_ButtonFrame, text="Cancel")

    optw.grid(row=1, column=1, padx=20, pady=10)
    opt_defaultDLLabel.grid(row=1, column=1, sticky="w")
    opt_defaultDLEntry.grid(row=2, column=1)
    opt_defaultDLButton.grid(row=2, column=2, padx=10)
    opt_ButtonFrame.grid(row=99, column=1, columnspan=2)
    # Part of opt_ButtonFrame:
    opt_SaveButton.grid(row=1, column=1, sticky="e", padx=3, pady=5)
    opt_CancelButton.grid(row=1, column=2, sticky="w", padx=3, pady=5)

# Menubar
menubar = tk.Menu(win)
# File
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Preferences", command=optWindowOpen)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=closeProgram)
menubar.add_cascade(label="File", menu=filemenu)
# Edit
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Delete")
editmenu.add_command(label="Select All")
menubar.add_cascade(label="Edit", menu=editmenu)
# Help
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Check for Updates")
helpmenu.add_command(label="View on GitHub")
helpmenu.add_command(label="About YTget", command=aboutWindowOpen)
menubar.add_cascade(label="Help", menu=helpmenu)
win.config(menu=menubar)

# Logo
fYTgetLogos = tk.Frame(win)
YTgetLogo = ImageTk.PhotoImage(Image.open("images/icon-90p.png"))
lYTgetLogo = tk.Label(fYTgetLogos, image=YTgetLogo)
YTgetTextLogo = ImageTk.PhotoImage(Image.open("images/Ytget-transparent.png"))
lYTgetTextLogo = tk.Label(fYTgetLogos, image=YTgetTextLogo)

# Grid and Pack cannot be used in the same frame. Due to the fact that the main
# window is also treated as a frame, I've decided to put the logo using pack inside
# the main window, and everything else using grid inside of a big frame titled "w".
w = tk.Frame(win)
w.option_add("*font", "Segoe")

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

linkLabel = tk.Label(w, text="Link to video:")
linkVar = tk.StringVar()
linkEntry = tk.Entry(w, textvariable=linkVar, width=69) #nice
linkVar.trace("w", validateLink)
validTextString = tk.StringVar() # Used by validateLink(), which is called everytime the Entry is modified.
validLabel = tk.Label(w, textvariable=validTextString)
# Put a bold font on the text.
bold_font = font.Font(validLabel, validLabel.cget("font"))
bold_font.configure(weight="bold")
validLabel.config(font=bold_font)

formatFrame = tk.Frame(w)
formatLabel = tk.Label(formatFrame, text="Format:")
downloadFormat = tk.StringVar()
audioButton = tk.Radiobutton(formatFrame, text="Audio", variable=downloadFormat, value="audio")
audioButton.select() # We need to have a default option selected.
videoButton = tk.Radiobutton(formatFrame, text="Video", variable=downloadFormat, value="video")

DLFrame = tk.Frame(w)
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
fYTgetLogos.grid(column=1, row=1)
lYTgetLogo.pack(side="left")
lYTgetTextLogo.pack(side="right")

w.grid(column=1, row=2, padx=20, pady=10)
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

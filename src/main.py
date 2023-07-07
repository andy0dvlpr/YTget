import os
import json
import webbrowser
import platform
import tkinter as tk
from tkinter import font
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

YTGET_VERSION = "3.0"
YTGET_OPTFOLDER = os.environ["APPDATA"] + "\\YTget"
OS_VER = platform.system() + " " + platform.release()

def loadSettings():
    if not os.path.exists(YTGET_OPTFOLDER):
        os.makedirs(YTGET_OPTFOLDER)
    # Read settings:
    try:
        optFile = open(YTGET_OPTFOLDER + "\\settings", "r")
    except FileNotFoundError:
        # The settings file does not exist, so initialize the settings blank.
        global defaultDL
        defaultDL = ""
        global enforceBitrate
        enforceBitrate = 0
        global bitrate
        bitrate = "192"
        global aExt
        aExt = "mp3"
        global vExt
        vExt = "mp4"
    else:
        # Load settings.
        try:
            globals().update(json.loads(optFile.read())) # Take the stored variables and load them.
        except:
            messagebox.showerror("Error reading settings file",
"""YTget settings have become corrupted, and will be reset.
Please relaunch the program.""")
            optFile.close()
            os.remove(YTGET_OPTFOLDER + "\\settings")
            os._exit(1)
loadSettings()

win = tk.Tk()
win.title("YTget " + YTGET_VERSION)
win.resizable(False, False)
window_icon = tk.PhotoImage(file = "images/icon-256p.png")
win.iconphoto(False, window_icon)

def closeProgram():
    win.destroy()

def checkUpdates():
    # TODO: Implement an actual update checking mechanism.
    webbrowser.open("https://github.com/andy0dvlpr/YTget/releases")

def openGitHub():
    webbrowser.open("https://github.com/andy0dvlpr/YTget")

def cutMenu():
    linkEntry.event_generate("<<Cut>>")

def copyMenu():
    linkEntry.event_generate("<<Copy>>")

def pasteMenu():
    linkEntry.event_generate("<<Paste>>")

def selallMenu():
    linkEntry.selection_range(0, tk.END)

def showContext(event):
    linkContext.post(event.x_root, event.y_root)

def aboutWindowOpen():
# About window
    aboutwin = tk.Toplevel(win)
    aboutwin.title("About YTget")
    aboutwin.resizable(False, False)
    aboutwin.iconphoto(False, window_icon)

    abtw = tk.Frame(aboutwin) # Frame for universal padding.
    # For some reason, the image isn't being displayed.
    # TODO: Fix
    # abt_YTgetLogo = ImageTk.PhotoImage(Image.open("images/icon-90p.png"))
    # abt_lYTgetLogo = tk.Label(abtw, image=abt_YTgetLogo)
    abt_aboutLabel = tk.Label(abtw, text="About YTget")
    abt_verLabel = tk.Label(abtw, text=f"You are currently running YTget {YTGET_VERSION}, under {OS_VER}.")
    abt_authorLabel = tk.Label(abtw, text="Software written by andy0dvlpr.")
    abt_legalLabel = tk.Label(abtw, font=("Arial", 8),
text="""THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.""")

    abtw.grid(row=1, column=1, padx=20, pady=10)
    # abt_lYTgetLogo.grid(row=1, column=1)
    abt_aboutLabel.grid(row=2, column=1)
    abt_verLabel.grid(row=3, column=1)
    abt_authorLabel.grid(row=4, column=1)
    abt_legalLabel.grid(row=5, column=1)


def optWindowOpen():
    optwin = tk.Toplevel(win)
    optwin.title("YTget Preferences")
    optwin.resizable(False, False)
    optwin.iconphoto(False, window_icon)

    optw = tk.Frame(optwin) # Frame for universal padding.
    opt_defaultDLFrame = tk.Frame(optw)
    opt_defaultDLLabel = tk.Label(opt_defaultDLFrame, text="Default save location:")
    opt_defaultDL = tk.StringVar()
    if not defaultDL: # If the setting is blank, use default:
        opt_defaultDL.set(os.environ["USERPROFILE"] + "\\Downloads")
    else:
        opt_defaultDL.set(defaultDL)
    opt_defaultDLEntry = tk.Entry(opt_defaultDLFrame, textvariable=opt_defaultDL, width=30)
    def opt_getDefaultDL():
        optwin.attributes("-topmost", 0) # Due to a tkinter bug, child windows go behind root windows when a file dialog opens.
        newDefaultDL = filedialog.askdirectory()
        optwin.attributes("-topmost", 1) # Now we set it back. This is how we circumvent the tkinter bug.
        if newDefaultDL: # If the user selected a folder
            opt_defaultDL.set(newDefaultDL)
    opt_defaultDLButton = tk.Button(opt_defaultDLFrame, text="Choose location", command=opt_getDefaultDL)
    opt_bitrateFrame = tk.Frame(optw)
    opt_enforceBitrate = tk.IntVar()
    opt_Bitrate = tk.StringVar()
    opt_Bitrate.set(bitrate)
    opt_BitrateEntry = tk.Entry(opt_bitrateFrame, textvariable=opt_Bitrate, state=tk.DISABLED)
    def opt_BitrateOnOff():
        if opt_enforceBitrate.get() == 0:
            opt_BitrateEntry.config(state=tk.DISABLED)
        elif opt_enforceBitrate.get() == 1:
            opt_BitrateEntry.config(state=tk.NORMAL)
    opt_bitrateCheck = tk.Checkbutton(opt_bitrateFrame, text="Enforce bitrate for audio", variable=opt_enforceBitrate, onvalue=1, offvalue=0, command=opt_BitrateOnOff)
    if enforceBitrate == 1:
        opt_bitrateCheck.select() # If enforceBitrate from settings file is 1, set the IntVar from tk to 1 as well by selecting it.
        opt_BitrateOnOff() # The function supplied in "command" for opt_bitrateCheck isn't run when using the select() method, so we need to do it manually.
    opt_kbpsLabel = tk.Label(opt_bitrateFrame, text="kbps")
    opt_extensionFrame = tk.Frame(optw)
    opt_aExtLabel = tk.Label(opt_extensionFrame, text="Audio format")
    opt_aExtOpt = ["mp3", "flac", "wav", "wma"]
    opt_aExtSel = tk.StringVar()
    opt_aExtSel.set(aExt)
    opt_aExtMenu = tk.OptionMenu(opt_extensionFrame, opt_aExtSel, *opt_aExtOpt)
    opt_aExtMenu.config(indicatoron=0)
    opt_vExtLabel = tk.Label(opt_extensionFrame, text="Video format")
    opt_vExtOpt = ["mp4", "mkv", "mov", "avi", "webm"]
    opt_vExtSel = tk.StringVar()
    opt_vExtSel.set(vExt)
    opt_vExtMenu = tk.OptionMenu(opt_extensionFrame, opt_vExtSel, *opt_vExtOpt)
    opt_vExtMenu.config(indicatoron=0)


    # OK and Cancel Buttons:
    def opt_SaveSettings():
        opt_Settings = {
            "defaultDL": opt_defaultDL.get(),
            "enforceBitrate": opt_enforceBitrate.get(),
            "bitrate": opt_Bitrate.get(),
            "aExt": opt_aExtSel.get(),
            "vExt": opt_vExtSel.get()
        }
        jsonSettings = json.dumps(opt_Settings)
        optFile = open(YTGET_OPTFOLDER + "\\settings", "w")
        optFile.write(jsonSettings)
        optFile.close()
        loadSettings() # Load the new settings.
        # Update the text of the audio and video radio buttons accordingly:
        audioButton["text"] = f"Audio ({aExt})"
        videoButton["text"] = f"Video ({vExt})"
        optwin.destroy()
    def opt_CancelSettings():
        optwin.destroy()
    opt_ButtonFrame = tk.Frame(optw)
    opt_SaveButton = tk.Button(opt_ButtonFrame, text="OK", command=opt_SaveSettings)
    opt_CancelButton = tk.Button(opt_ButtonFrame, text="Cancel", command=opt_CancelSettings)

    optw.grid(row=1, column=1, padx=20, pady=10)
    
    opt_defaultDLFrame.grid(row=1, column=1, pady=10)
    # Part of opt_defaultDLFrame:
    opt_defaultDLLabel.grid(row=1, column=1, sticky="w")
    opt_defaultDLEntry.grid(row=2, column=1)
    opt_defaultDLButton.grid(row=2, column=2, padx=(10, 0))

    opt_bitrateFrame.grid(row=2, column=1, pady=10)
    # Part of opt_bitrateFrame
    opt_bitrateCheck.grid(row=1, column=1)
    opt_BitrateEntry.grid(row=1, column=2)
    opt_kbpsLabel.grid(row=1, column=3)

    opt_extensionFrame.grid(row=3, column=1, pady=10)
    # Part of opt_extensionFrame
    opt_aExtLabel.grid(row=1, column=1)
    opt_aExtMenu.grid(row=1, column=2)
    opt_vExtLabel.grid(row=1, column=3)
    opt_vExtMenu.grid(row=1, column=4)

    opt_ButtonFrame.grid(row=99, column=1, columnspan=2, pady=(10, 5))
    # Part of opt_ButtonFrame:
    opt_SaveButton.grid(row=1, column=1, sticky="e", padx=3)
    opt_CancelButton.grid(row=1, column=2, sticky="w", padx=3)

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
editmenu.add_command(label="Cut", command=cutMenu)
editmenu.add_command(label="Copy", command=copyMenu)
editmenu.add_command(label="Paste", command=pasteMenu)
editmenu.add_command(label="Select All", command=selallMenu)
menubar.add_cascade(label="Edit", menu=editmenu)
# Help
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Check for Updates", command=checkUpdates)
helpmenu.add_command(label="View on GitHub", command=openGitHub)
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
linkContext = tk.Menu(w, tearoff=0)
linkContext.add_command(label="Cut", command=cutMenu)
linkContext.add_command(label="Copy", command=copyMenu)
linkContext.add_command(label="Paste", command=pasteMenu)
linkContext.add_command(label="Select All", command=selallMenu)
linkEntry.bind("<Button-3>", showContext)
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
audioButton = tk.Radiobutton(formatFrame, text=f"Audio ({aExt})", variable=downloadFormat, value="audio")
audioButton.select() # We need to have a default option selected.
videoButton = tk.Radiobutton(formatFrame, text=f"Video ({vExt})", variable=downloadFormat, value="video")

DLFrame = tk.Frame(w)
DLLabel = tk.Label(DLFrame, text="Download location:")
DLOptions = [f"Default location ({defaultDL})", "Choose another location..."]
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

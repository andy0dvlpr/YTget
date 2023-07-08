import os
from yt_dlp import YoutubeDL

def downloader_loc(DLSel, DLOptions, defaultDL):
    if DLSel != DLOptions[0]: # If the user changed the download location through the menu on the main window
            return os.path.join(DLSel, "%(title)s.%(ext)s")
    else:
            return os.path.join(defaultDL, "%(title)s.%(ext)s")

def downloader(linkVar, downloadFormat, aExt, vExt, enforceBitrate, bitrate, DLSel, DLOptions, defaultDL):
    if downloadFormat == "audio":
        postprocessor = {
            "key": "FFmpegExtractAudio",
            "preferredcodec": aExt,
        }
        ytdl_opts = {
            "final_ext": aExt,
            "format": "bestaudio/best",
            "postprocessors": [postprocessor],
            "outtmpl": downloader_loc(DLSel, DLOptions, defaultDL)
        }
        if enforceBitrate == 1:
            postprocessor["preferredquality"] = bitrate
    
    if downloadFormat == "video":
        ytdl_opts = {
            "outtmpl": downloader_loc(DLSel, DLOptions, defaultDL),
        }
        if vExt == "Auto":
             ytdl_opts["format"] = "bv+ba" # best video + best audio
        else:
             ytdl_opts["format"] = f"bv[ext={vExt}]+ba/{vExt}" # chooses best version of chosen format + best audio

    with YoutubeDL(ytdl_opts) as ytdl:
        ytdl.download(linkVar)
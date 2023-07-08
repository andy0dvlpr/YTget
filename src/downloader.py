import os
from yt_dlp import YoutubeDL

def downloader(linkVar, downloadFormat, aExt, vExt, enforceBitrate, bitrate, DLSel, DLOptions, defaultDL):
    if downloadFormat.get() == "audio":
        postprocessor = {
            "key": "FFmpegExtractAudio",
            "preferredcodec": aExt,
        }
        ytdl_opts = {
            "final_ext": aExt,
            "format": "bestaudio/best",
            "postprocessors": [postprocessor],
        }
        if enforceBitrate == 1:
            postprocessor["preferredquality"] = bitrate
        if DLSel.get() != DLOptions[0]: # If the user changed the download location through the menu on the main window
            ytdl_opts["outtmpl"] = os.path.join(DLSel.get(), "%(title)s." + aExt)
        else:
            ytdl_opts["outtmpl"] = os.path.join(defaultDL, "%(title)s." + aExt)
    
    print(ytdl_opts)
    with YoutubeDL(ytdl_opts) as ytdl:
        ytdl.download(linkVar.get())
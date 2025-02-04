import tkinter as tk
from pytube import YouTube
import customtkinter
# Import the necessary modules

# Download function
def start_download(option):
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        if option == "highQuality":
            video = ytObject.streams.get_highest_resolution()
        elif option == "lowQuality":
            video = ytObject.streams.get_lowest_resolution()
        elif option == "audio":
            video = ytObject.streams.get_audio_only()
        else:
            return

        title.configure(text=ytObject.title, text_color="white")
        finishlabel.configure(text="")
        video.download(output_path="E:/BOOST")
        finishlabel.configure(text="Download Complete !!", text_color="green")

    except:
        finishlabel.configure(text="Download Error !!", text_color="Red")


# progress bar function

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining
    percentage_of_completion = bytes_download / total_size * 100
    per = str(int(percentage_of_completion))
    progress.configure(text=per + '%')
    progress.update()

    # update progress bar
    progressbar.set(float(percentage_of_completion) / 100)


# system settings

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# Application Frame

app = customtkinter.CTk()
app.geometry("1400 * 788")
app.title("Hank Youtube Downloader")

# logo
# app_icon = "C:\\Users\\Administrator\\Desktop\\100dayscode\\Youtube-video-downloader\\osint.jpg"

#  add UI elements
# app.iconbitmap(app_icon) the icon

title = customtkinter.CTkLabel(app, text="Insert a Youtube Link", width=200, height=50, font=("cursive", 28))
title.pack(padx=10, pady=10)

# link input
url_var = tk.StringVar()
link = customtkinter.CTkEntry(app, width=500, height=50, textvariable=url_var)
link.pack()

# Finished Downloading
finishlabel = customtkinter.CTkLabel(app, text="")
finishlabel.pack()

# Progress percentage
progress = customtkinter.CTkLabel(app, text="0%")
progress.pack()

# ProgressBar
progressbar = customtkinter.CTkProgressBar(app, width=400)
progressbar.set(0)
progressbar.pack(padx=10, pady=10)

# Download High Quality
download_hq = customtkinter.CTkButton(app, text="Download High Quality MP4",
                                      command=lambda: start_download("highQuality"))
download_hq.pack(padx=10, pady=10)

# Download Low Quality
download_lq = customtkinter.CTkButton(app, text="Download Low Quality MP4",
                                      command=lambda: start_download("lowQuality"))
download_lq.pack(padx=10, pady=10)

# Download Audio
download_audio = customtkinter.CTkButton(app, text="Download Audio - MP3", command=lambda: start_download("audio"))
download_audio.pack(padx=10, pady=10)

# Main loop

app.mainloop()

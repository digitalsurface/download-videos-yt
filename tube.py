import tkinter as tk
import pytube

def download_video():
    url = entry_url.get()
    video = pytube.YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download()

root = tk.Tk()
root.title("YouTube Downloader")

label = tk.Label(root, text="Digite o URL do vídeo:")
label.pack()

entry_url = tk.Entry(root, width=50)
entry_url.pack()

button = tk.Button(root, text="Baixar vídeo", command=download_video)
button.pack()

root.mainloop()

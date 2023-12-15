import tkinter as tk
from tkinter import messagebox

import pytube



def download_video():
    url = url_entry.get()
    try:
        video=pytube.YouTube(url)
        stream=video.streams.get_highest_resolution()
        stream.download()
        messagebox.showinfo('success','Video Downloaded Successfuly')
    except Exception as e:
        messagebox.showerror('Error',f'An error occurred:{str(e)}')

root=tk.Tk()
root.geometry('400x200')
root.title('YOUTUBE VIDEO DOWNLOADER WITH PD')
url_label=tk.Label(root,text="Enter Youtube Video URL", font=('Arial',14))
url_label.pack(pady=10)
url_entry=tk.Entry(root,width=50,font=("Arial",14))
url_entry.pack(pady=10)
download_button=tk.Button(root,text="Download",font=("Arial",14), command=download_video)
download_button.pack(pady=10)

chanel_label=tk.Label(root,text="Visit our Youtube chanel:   www.youtube.com/@Rule_Crafter",font=("Arial",7))
chanel_label.pack(pady=15)
root.mainloop()
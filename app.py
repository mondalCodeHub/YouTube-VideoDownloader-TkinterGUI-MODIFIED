from linecache import clearcache
from textwrap import fill
from tkinter import *
from tkinter import font
from turtle import clear
from typing import ForwardRef
from click import command
from pytube import YouTube
from tkinter import messagebox, filedialog
# 
def widgets_tk():

    head_text = Label(root, text="YouTube Video Downloader (V01)", padx=15, pady=15,font="luicda 16 bold ", bg='orange red',foreground='navajo white' )
    head_text.grid(row=1, column=1, pady=20, padx=5, columnspan=3)
    # head_text.pack(pady=20, padx=5)

    link_text = Label(root, text= "YouTube Link",padx=4, pady=4 , bg='orange red')
    link_text.grid(row=2, column=0, padx=4, pady=4)

    root.pasteLinkText = Entry(root, width=56 , textvariable=video_Link, font='luicda 16', background='snow3')
    root.pasteLinkText.grid(row=2, column= 1, padx=4, pady=4)

    destination_text = Label(root, text="  Destination   ", padx=4, pady=4 , bg='orange red')
    destination_text.grid(row=3, column= 0 , padx=8, pady=4)

    root.selectDestination = Entry(root, width=45, textvariable=download_Path,font='luicda 16', background='snow3' )
    root.selectDestination.grid(row=3, column=1, padx=4, pady=4)

    browse_destination = Button(root, text="Browse", font='luicda 13', background='orange red', command=browseFile,  relief=GROOVE)
    browse_destination.grid(row=3, column=2, padx=1, pady=1)

    downloadButton = Button(root, text="Download Video", font='lucida 16 bold', bg='green', foreground='white' , relief=GROOVE,padx=7, pady=7 , command=download)
    downloadButton.grid( row=4, column=1 , padx=15, pady=15)

    quitButton = Button (root, text="Quit Application",command=quit, bg='red', foreground='white', font='luicda 10 bold').grid(row=6, column=1)

# Browse location function 
def browseFile():
    download_dir = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video")
    download_Path.set(download_dir)

# dowmload function():
def download():
    youtubeVideoLink = video_Link.get()
    downloadFolderLocation = download_Path.get()
    # obj
    getVideo = YouTube(youtubeVideoLink)
    videostream = getVideo.streams.first()
    videostream.download(downloadFolderLocation)
    # display message using 'tmsg'
    messagebox.showinfo("SUCCESSFULL", f"Downloaded and Saved successfully in ' {downloadFolderLocation} ' ")

# GUI ##
root = Tk()
root.geometry("933x433")
root.title("YouTube Video Downloader BY @mondalCodeHub")
root.config(background='skyblue')
root.resizable(False, False)
root.wm_iconbitmap('icon.ico')
# 
# Entry
video_Link = StringVar()
download_Path = StringVar()
# Function call
widgets_tk()
root.mainloop()
# Created By : Arup Mondal (@MondalCodeHub)
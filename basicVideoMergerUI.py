from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

from moviepy.editor import *
import os

from datetime import datetime

def pickFiles():
    path = filedialog.askopenfile(title="Select file",filetypes=(("MP4", "*.MP4"),("all files", "*.*")))
    fileList.append(path)
    pathTemp = path.name.split("/")
    listbox.insert(END, pathTemp[len(pathTemp)-1])

def deleteSelected():
    selection = listbox.curselection()
    print(selection)
    if len(selection)>0:
        listbox.delete(selection[0])
        fileList.pop(selection[0])

def clearList():
    fileList = []
    listbox.delete(0,END)

def processVideos():
    try:
        print("generating file: "+outputEntry.get()+".MP4")
        videoList =[]
        for file in fileList:
            video = VideoFileClip(file.name)
            videoList.append(video)

        final_clip = concatenate_videoclips(videoList)
        if outputEntry.get()!="":
            outputName = outputEntry.get()  
        else: 
            outputName = str(datetime.now(tz=None)).replace(" ","").replace(".","").replace(":","").replace("-","")
            outputEntry.insert(0,outputName)
        print("outputName:"+outputName)
        final_clip.to_videofile(outputName+".MP4", remove_temp=False)

    except Exception as e: 
        print(e)


window = Tk()
window.title("Video Merge")
window.resizable(True, True)
window.geometry('300x500')

fileList = []
select1Button = Button(window, text="Select a file", command=pickFiles)
select1Button.place(x=5, y=5, width=80)
deleteButton = Button(window, text="delete", command=deleteSelected)
deleteButton.place(x=90, y=5, width=80)
clearButton = Button(window, text="clear", command=clearList)
clearButton.place(x=5, y=40, width=80)
processButton = Button(window, text="process", command=processVideos)
processButton.place(x=90, y=40, width=80)
labelOutputName = Label(window, text="Output file name:")
labelOutputName.place(x=5, y=75)
outputEntry = ttk.Entry(window, width=30)
outputEntry.place(x=5, y=100)
labelFiles = Label(window, text="Files:")
labelFiles.place(x=5, y=145)
listbox = Listbox(window)
listbox.place(x=5, y=170, width=200)
window.mainloop()

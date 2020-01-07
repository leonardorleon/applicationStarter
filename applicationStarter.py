#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog, Text
import subprocess

# create the base of the GUI
root = tk.Tk()
apps = []

# function that opens up a file dialog which lets the user select application files
def addApp():
    
    # first destroy any widgets that were previously placed in the frame
    for widget in frame.winfo_children():
        widget.destroy()
    
    filename = filedialog.askopenfilename(initialdir="/usr/share/applications", title="Select file",
                                          filetypes=(("shortcuts","*.desktop"), ("all files","*.*")))
    # filenames are stored on a list
    filename = filename.split("/")[-1].split(".")[0]
    print(filename)
    apps.append(filename)
    # for each app on the list, place a text label with the filename of the application
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def startApps():
    for app in apps:
        subprocess.call(["gtk-launch",app])


# root.configure(bg="white")
root["bg"] = "white"

# create a colored canvas to work as the base of the elements
canvas = tk.Canvas(root, height=600, width=600, bg="#569a40")
canvas.pack()

# frame to display the aplications
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# button to open the file dialog to add an app to the list
openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="#569a40", command=addApp)
openFile.pack()

# button that starts all the apps added to the list
startApps = tk.Button(root, text="Start Applications", padx=10,
                      pady=5, fg="white", bg="#569a40", command=startApps)
startApps.pack()

root.mainloop()

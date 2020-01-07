#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog, Text
import subprocess
import os

# create the base of the GUI
root = tk.Tk()
apps = []

# if the save.txt file exists in the path of the application, it loads the names on the text file to the app list
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

# function that opens up a file dialog which lets the user select application files
def addApp():
    
    # first destroy any widgets that were previously placed in the frame so the list is not repeated
    for widget in frame.winfo_children():
        widget.destroy()
    
    filename = filedialog.askopenfilename(initialdir="/usr/share/applications", title="Select file",
                                          filetypes=(("shortcuts","*.desktop"), ("all files","*.*")))
    filename = filename.split("/")[-1].split(".")[0]
    # filenames are stored on a list
    if( len(filename) > 0) : apps.append(filename)
    # write the name of the applications to the frame.
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

# When the program is first loaded, if the save.txt file had names they were loaded to apps. Here we list them on startup
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
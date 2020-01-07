#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog, Text
import os

# create the base of the GUI
root = tk.Tk()
apps = []

def addApp():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("shortcuts","*.desktop"), ("all files","*.*"), ("executables","*.exe")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

# root.configure(bg="white")
root["bg"] = "white"

# create a colored canvas to work as the base of the elements
canvas = tk.Canvas(root, height=600, width=600, bg="#569a40")
canvas.pack()

# frame to display the aplications
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="#569a40", command=addApp)

openFile.pack()

startApps = tk.Button(root, text="Start Applications", padx=10,
                      pady=5, fg="white", bg="#569a40")
startApps.pack()

root.mainloop()

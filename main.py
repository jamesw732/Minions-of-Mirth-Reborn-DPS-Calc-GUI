from tkinter import *
from tkinter import ttk
from typing import Container
from colors import *
from damagecalc import *

root = Tk()
root.title("DPS Calc")
root.configure(bg="#282828")

entries = [Entry(root, width=12, bg=grey, fg=text) for x in range(8)]

def start():
    setLastLine()
    Label(root, text='Tracking DPS', bg=grey, fg=text).grid(column=4, row=0)
    for entry in entries:
        entry.delete(0, END)   

def displayStats(playerName):
    stats = getStats(playerName)
    Label(root, width=10, bg=grey, fg=text).grid(column=4, row=0)
    if stats[0] > 0:
        entries[0].insert(0, stats[0]) # total damage
        dmgList = stats[2]
        entries[1].insert(0, len(dmgList)) # number of hits
        entries[2].insert(0, min(dmgList)) # min hit
        entries[3].insert(0, max(dmgList)) # max hit
        entries[4].insert(0, int(entries[0].get())/int(entries[1].get()))  # avg hit
        entries[5].insert(0, stats[1]) # elapsed time
        entries[6].insert(0, int(entries[0].get()) / float(entries[5].get())) # DPS
        entries[7].insert(0, float(entries[6].get()) * 60) # DPM
    else:
        entries[0].insert(0, "Try Again")

def createInputFrame(container):
    frame = ttk.Frame(container)
    Label(container, text='Name:', bg=grey, fg=text).grid(column=0, row=0)
    name = Entry(container, width=12, bg=grey, fg="cyan")
    name.focus()
    name.grid(column=1, row=0)
    startButton = Button(container, text='Start', activebackground=hoverBG, activeforeground=hoverText, bg=brown, command=start).grid(column=2, row=0)
    stopButton = Button(container, text='Stop', activebackground=hoverBG, activeforeground=hoverText, bg=brown, command= lambda: displayStats(name.get())).grid(column=3, row=0)
    return frame

def createOutputFrame(container):
    frame = ttk.Frame(container)
    cols = ["Damage", "# Hits", "Min Hit", "Max Hit", "Avg Hit", "Time (s)", "DPS", "DPM"]
    for i in range(8):
        Label(container, text=cols[i], bg=grey, fg=text).grid(column=i,row=1)
    
    for j in range(8):
        entries[j].grid(column=j,row=2)
    
    return frame

def createMainWindow():
    createOutputFrame(root)
    createInputFrame(root)
    
    root.mainloop()

createMainWindow()


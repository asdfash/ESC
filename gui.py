import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
import os
import functions



#start script, pull config data
filename = os.path.basename("__file__")
workingdir = "__file__"[:len("__file__")-len(filename)]
config = workingdir + 'config.txt'
defauloutput = workingdir
defaultlog = workingdir + "logs/"

excelpath = ""
gdbpath = ""
outputpath = defauloutput
logpath= defaultlog

try:
    f = open("config.txt","r")
    configtext =f.read().split(" ")
    f.close()
    excelpath = configtext[0]
    gdbpath= configtext[1]
    outputpath= configtext[2]
    logpath = configtext[3]
    
except:
    print("error, rebuilding config file with defaults")
    f = open("config.txt","w")
    f.write(excelpath + " " + gdbpath + " " + outputpath + " " + logpath)
    f.close()

#helper functions
def runhelp():
    functions.main(excelpath,gdbpath,outputpath,logpath)

def excelask():
    global excelpath
    excelpath = filedialog.askopenfilename(initialdir=workingdir, filetypes=[("Excel files", "*.xlsx")])
    f = open("config.txt","w+")
    f.write(excelpath + " " + gdbpath + " "+ outputpath + " " + logpath)
    f.close()
    excelpathtext['text'] = excelpath

def gdbask():
    global gdbpath
    gdbpath = filedialog.askdirectory(initialdir=workingdir)
    f = open("config.txt","w+")
    f.write(excelpath + " " + gdbpath + " "+ outputpath + " " + logpath)
    f.close()
    gdbpathtext['text'] = gdbpath

def outputask():
    global outputpath
    outputpath = filedialog.askdirectory(initialdir=defauloutput) + '/'
    f = open("config.txt","w+")
    f.write(excelpath + " " + gdbpath + " "+ outputpath + " " + logpath)
    f.close()
    outputpathtext['text'] = outputpath

def logask():
    global logpath
    logpath = filedialog.askdirectory(initialdir=workingdir) + '/'
    f = open("config.txt","w+")
    f.write(excelpath + " " + gdbpath + " "+ outputpath + " " + logpath)
    f.close()
    logpathtext['text'] = logpath

#draw windows
root =tk.Tk()
mainframe= ttk.Frame(padding=10)
excelframemain = ttk.Frame(master=mainframe)
excelframelabel= ttk.Frame(master=excelframemain)
excelframebutton = ttk.Frame(master=excelframemain)
excellabel = ttk.Label(master =excelframelabel, text="Excel sheet file location",width=50,padding=5)
excellabel.pack()
excelpathtext = ttk.Label(master =excelframelabel, text=excelpath,width=50)
excelpathtext.pack()
excelframelabel.pack(side=tk.LEFT)
excelbutton = ttk.Button( master =excelframebutton, text="select file",width=15,command=excelask)
excelbutton.pack()
excelframebutton.pack(side=tk.RIGHT)
excelframemain.pack(fill=tk.BOTH)

gdbframemain = ttk.Frame(master=mainframe)
gdbframelabel= ttk.Frame(master=gdbframemain)
gdbframebutton = ttk.Frame(master=gdbframemain)
gdblabel = ttk.Label(master =gdbframelabel, text="gdb sheet file location",width=50,padding=5)
gdblabel.pack()
gdbpathtext = ttk.Label(master =gdbframelabel, text=gdbpath,width=50)
gdbpathtext.pack()
gdbframelabel.pack(side=tk.LEFT)
gdbbutton = ttk.Button( master =gdbframebutton, text="select file",width=15, command= gdbask)
gdbbutton.pack()
gdbframebutton.pack(side=tk.RIGHT)
gdbframemain.pack(fill=tk.BOTH)

outputframemain = ttk.Frame(master=mainframe)
outputframelabel= ttk.Frame(master=outputframemain)
outputframebutton = ttk.Frame(master=outputframemain)
outputlabel = ttk.Label(master =outputframelabel, text="output sheet folder location",width=50,padding=5)
outputlabel.pack()
outputpathtext = ttk.Label(master =outputframelabel, text=outputpath,width=50)
outputpathtext.pack()
outputframelabel.pack(side=tk.LEFT)
outputbutton = ttk.Button( master =outputframebutton, text="select folder",width=15, command=outputask)
outputbutton.pack()
outputframebutton.pack(side=tk.RIGHT)
outputframemain.pack(fill=tk.BOTH)

logframemain = ttk.Frame(master=mainframe)
logframelabel= ttk.Frame(master=logframemain)
logframebutton = ttk.Frame(master=logframemain)
loglabel = ttk.Label(master =logframelabel, text="log folder location",width=50,padding=5)
loglabel.pack()
logpathtext = ttk.Label(master =logframelabel, text=logpath,width=50)
logpathtext.pack()
logframelabel.pack(side=tk.LEFT)
logbutton = ttk.Button( master =logframebutton, text="select folder",width=15, command= logask)
logbutton.pack()
logframebutton.pack(side=tk.RIGHT)
logframemain.pack(fill=tk.BOTH)

run = ttk.Button(text="run",master=mainframe,command=runhelp)
run.pack(fill= tk.BOTH)
mainframe.pack(fill=tk.BOTH)
root.mainloop()


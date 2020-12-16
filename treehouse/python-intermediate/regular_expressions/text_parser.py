import re
import sys
from tkinter import Tk

print("Enter the data") 
data = sys.stdin.read()   # Use Ctrl d to stop the input 

matches = re.findall(r"Message by .*", data)

string = "\n".join(matches)

r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(string)
r.update() # now it stays on the clipboard after the window is closed
r.destroy()

print("Text conversation is ready to paste (It's already on your clipboard. Just hit cmd+v into the log).\nHere is the correctly formated message\n***********")
print(string)
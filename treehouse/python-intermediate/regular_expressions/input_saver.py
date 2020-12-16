import sys 
print("Enter the data") 
data = sys.stdin.read()   # Use Ctrl d to stop the input 
print(data) 

f = open("textsample.txt", "w")
f.write("")
f.close()
    
f = open("textsample.txt", "a")
f.write(data)
f.close()




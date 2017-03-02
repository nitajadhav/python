"read file and print"

#open
file=open("file.txt","r+")

#read
print("file name",file.name)
text=file.read();
print("text",text)

#write
file.write("some new text inserted*******")
file.seek(0)
print("\n\nafter updation",file.read())
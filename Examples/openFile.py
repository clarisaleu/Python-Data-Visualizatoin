#standard way of dealing with files
#write to file . run and create file
f = open("myfile.txt","w")

f.write("Hello")
f.close()

#append mode
f = open("myfile.txt","a")
f.write(" World. you're a hoss boss")
f.write("Again")
f.write("\n")
f.write(str(400)) #convert 400 to str
f.close()

#read mode
f = open("myfile.txt","r")
line = f.readline(190)
print(line)

print(line.strip("\n"))
print(line.strip("\n").split(" "))
print(line)
print(int("1"))
f.close()

#better way. don't have to worry about closing files
with open("myfile.txt","r") as f:
     line2 = f.readline()
     print(line2)

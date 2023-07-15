f = open('texts.txt',"r")
words = 0
letters = 0
lines = 0
for line in f:
    lines += 1
    line = line.strip("\n")
    letters += len(line)
    list = line.split()
    words += len(list)
print(lines,letters,words)
f.close()
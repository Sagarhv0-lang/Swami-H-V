f = open("test.txt", 'r')
line_count = 0
for line in f:
    line_count += 1
f.close()
print("Number of lines in the file:", line_count)

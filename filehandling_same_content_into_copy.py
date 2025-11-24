with open("test.txt", 'r') as src:
    content = src.read()  
with open("copy.txt", 'w') as dest:
    dest.write(content)    

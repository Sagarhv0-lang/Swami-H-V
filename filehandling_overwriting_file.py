with open("test.txt", 'w') as f:
    f.write("This will overwrite the file.\n")
    f.write("All previous content is gone.\n")
print("File has been overwritten.")

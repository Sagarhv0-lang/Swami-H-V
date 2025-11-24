user_text = input("Enter some text: ")
with open("test.txt", 'w') as f:
    f.write(user_text)


db = open("output.txt", "a")
a = "Hello" + "1"   # fixed: string concatenation only works with strings
b = "How do you do?"
db.write(a + ", " + b + "\n")
db.close()  # good practice to close the file
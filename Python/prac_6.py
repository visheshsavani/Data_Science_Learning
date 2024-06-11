# f = open("prac.txt","w")
# f.write("Hi everyone\nwe are learning File I/O\nusing JAVA\nI like programming in JAVA")
with open("prac.txt","r") as f:
    data = f.read()
import os
os.mkdir("d")
os.mkdir("e")
print(os.getcwd())
os.chdir("d")
print(os.getcwd())
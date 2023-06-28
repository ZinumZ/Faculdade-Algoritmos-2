import os
os.chdir("a")
print(os.getcwd())
os.chdir("..") #Diretório superior
print(os.getcwd())
os.chdir("b")
print(os.getcwd())
os.chdir("../c")
print(os.getcwd())

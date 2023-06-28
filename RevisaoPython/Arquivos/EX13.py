import os
open("moribundo.txt", "w").close()
os.mkdir("vago")
os.rmdir("vago")
os.remove("moribundo.txt")

print("Sucesso")
import os



direc = os.listdir(os.getcwd())
atual = os.getcwd()
direc.remove(".git")

for f in direc:
    if(os.path.isdir(f)):
        os.system("rm -rf " + f)
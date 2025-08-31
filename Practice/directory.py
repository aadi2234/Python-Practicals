import os
print(os.getcwd())
os.mkdir("Test")
print(os.listdir())
os.chdir("Test","Demo")
os.rmdir("Demo")
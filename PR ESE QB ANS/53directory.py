#53.	Create a directory named “first_dir” and apply various directory handling methods in Python on it.
import os
os.mkdir('first_dir')
print("Current Working Directory:",os.getcwd())
print("List Directory:",os.listdir())
print('Renamed Directory',os.rename('first_dir','Sample'))
print("Removed Directory",os.rmdir('PWP'))
print("Changed Directory",os.chdir('Practice'))
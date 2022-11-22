import random,os

p='/home/saarthak'

"""To change the current working directory to the path given"""

os.chdir(p) # To change to the specified directory path
# print(os.listdir(p))
folder_name=random.choice(os.listdir(p))
folder_path=str(os.path.realpath(folder_name))
file_name= random.choice([f for f in os.listdir(p) if os.path.isfile(os.path.join(p,f))])
print("Enjoy")

# To play the file
#os.system deals with os operations
os.system("xdg-open " + file_name)
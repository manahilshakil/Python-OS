#os
#make,change,current,remove,rename,size
# path.time,isdir,join

import os

def write_file(filename,list):
    with open(filename,"w") as file:
        for i in list:
            file.write(i +"\n")

    print("Data written, the size is now {}".format(os.path.getsize(filename)))

def change_directory(directory):
    current = os.getcwd()
    os.chdir(directory)
    with open("test.txt","r") as file:
        pass
    new = os.getcwd()
    print("New directory: {}".format(new))

import os
def check_directory(directories):
    for directory in directories:
        if os.path.isdir(directory):
            print("Valid directory")
        else:
            print("Directory not found")
#This function creates a new python script in the
# current working directory add the line of comments to it declared by the comments variable and
# returns the size of the new file fill in the gas to create a script called program.py
import os

def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as script_file:
        script_file.write(comments)

    filesize = os.path.getsize(filename)
    return filesize

print(create_python_script("program.py"))

#next
import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename,"w") as file:
    pass

  # Return the list of files in the new directory
  return os.listdir()

print(new_directory("PythonPrograms", "script.py"))

#next
import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, "w") as file:
        pass
  timestamp = os.path.getctime(filename)
  # Convert the timestamp into a readable format, then into a string
  date_created = datetime.datetime.fromtimestamp(timestamp)
  # Return just the date portion
  # Hint: how many characters are in “yyyy-mm-dd”?
  return ("{:%Y-%m-%d}".format(date_created))

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd

#nwxt
import os
def parent_directory():
  # Create a relative path to the parent
  # of the current working directory
  relative_parent = os.path.join('..', os.getcwd())

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

print(parent_directory())
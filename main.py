"""Delete all files in a directory that are older than a specified time.
"""
    
import os
import sys
import time
import ctypes

def get_is_admin():
    """Get the UAC level.
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return "Could not get the UAC level."
    
def set_admin():
    """Set the UAC level to admin.
    """
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    except:
        print("Could not set the UAC level.")

def main():
    """Delete all files in a directory that are older than a specified time.
    """
    # Get the directory name.
    print("Give me the name of the directory.")
    dir_name = input("? ")
    # Get the age in days.
    print("Give me the age in days.")
    age = int(input("? "))
    # Get the current time.
    current_time = os.path.getmtime(dir_name)
    # Get the file names in the directory.
    file_names = os.listdir(dir_name)
    # Delete the files.
    for file_name in file_names:
        file_path = os.path.join(dir_name, file_name)
        file_time = os.path.getmtime(file_path)
        if (current_time - file_time) > age:
            os.remove(file_path)
    
    


if get_is_admin() == True:
    main()
else:
    do_you_want_to_be_admin = input("Do you want to be admin? (y/n) ")
    if do_you_want_to_be_admin == "y":
        set_admin()
    else:
        print("You are not admin.")



# wait 10 seconds
time.sleep(10)
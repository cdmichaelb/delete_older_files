"""Delete all files in a directory that are older than a specified time.

        for file_name in file_names:
            file_path = os.path.join(dir_name, file_name)
            
            file_time = os.path.getmtime(file_path)
        
            current_age = (current_time - file_time)/24/60/60
            if current_age > age:
                print(f'Deleting file: {file_name} in {dir_name} because {round(current_age, 0)} is older than {age} days.')
                os.chmod(file_path, 0o777)
                os.remove(file_path)
            else:
                print(f'Keeping file: {file_name} in {dir_name} because {round(current_age, 0)} is not older than {age} days.')

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
    still_work_to_do = True
    each_dir = "None"
    while still_work_to_do:
        if each_dir == "None":
            still_work_to_do, each_dir = do_delete(dir_name, age)
        elif not each_dir == "None":
            still_work_to_do, each_dir = do_delete(each_dir, age)

            
def do_delete(dir_name, age, recursion=None):
    try:
        each_directory = False
            # Get the current time.
        current_time = time.time()
        #current_time = os.path.getmtime(dir_name)
        # Get the file names in the directory.
        if recursion == None:
            file_names = os.listdir(dir_name)
        
        # Make a seperate list for directories.
        
        dir_names = [dir_name + "/" + file_name for file_name in file_names if os.path.isdir(dir_name + "/" + file_name)]
        
        # Remove directories from file_names
        #file_names = [file_name for file_name in file_names if not os.path.isdir(os.path.join(dir_name, file_name))]
        #print(f'{dir_name} has {len(file_names)} files and {len(dir_names)} directories.')
        # Delete the files.
        for each_directory in dir_names:
            print("Deleting files in " + each_directory + "...")
            for each_file in os.listdir(each_directory):
                if os.path.getmtime(each_directory + "/" + each_file) < current_time - age * 86400:
                    print(f"Deleting file: {each_file} in {each_directory} because {os.path.getmtime(each_directory + '/' + each_file)} is older than {current_time - age * 8640} days.")
                    os.chmod(each_directory + "/" + each_file, 0o777)
                    os.remove(each_directory + "/" + each_file)
                    each_directory.remove(each_file)
            # Delete the directory.
            if os.rmdir(each_directory):
                os.chmod(each_directory, 0o777)
                dir_names.remove(each_directory)
                print(f"Deleting directory: {each_directory}.")
        do_delete(dir_name, age)
    except FileNotFoundError:
        print("The directory or file does not exist.")
    except RecursionError:
        print("Maximum depth exceeded.")
        if each_directory == "None":
            return True, "None"
        else:
            return True, each_directory
    except os.error:
        print(f"Access denied. {each_file} {each_directory}")
        if each_directory:
            do_delete(each_directory, age)
    except UnboundLocalError as e:
        print("Unbound Local Error", e)
        quit()
    except Exception as e:
        print(e)
        if each_directory:
            do_delete(each_directory, age)
    if recursion:
        recursion = None
        return True, "None"
    # If there are no more directories to delete, return False.
    elif not each_directory:
        return False, "None"
    return True, "None"
    
main()

""" if get_is_admin() == True:
    main()
else:
    do_you_want_to_be_admin = input("Do you want to be admin? (y/n) ")
    if do_you_want_to_be_admin == "y":
        set_admin()
    else:
        print("You are not admin.") """



# wait 10 seconds
time.sleep(1)
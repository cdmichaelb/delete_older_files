"""Delete all files in a directory that are older than a specified time.
"""

import os
import time


def main():
    """Delete all files in a directory that are older than a specified time."""
    # Get the directory name.
    print("Give me the name of the directory.")
    dir_name = input("? ")
    # Get the age in days.
    print("Give me the age in days.")
    age = int(input("? "))
    still_work_to_do = True
    each_dir = None
    while still_work_to_do:
        if each_dir == None:
            still_work_to_do, each_dir = do_delete(dir_name, age)
        elif not each_dir == None:
            still_work_to_do, each_dir = do_delete(each_dir, age)


def do_delete(dir_name, age, recursion=None):
    try:
        each_directory = False
        # Get the current time.
        current_time = time.time()
        # current_time = os.path.getmtime(dir_name)
        # Get the file names in the directory.
        if recursion == None:
            file_names = os.listdir(dir_name)

        # Make a seperate list for directories.

        dir_names = [
            dir_name + "/" + file_name
            for file_name in file_names
            if os.path.isdir(dir_name + "/" + file_name)
        ]

        # Remove directories from file_names
        # file_names = [file_name for file_name in file_names if not os.path.isdir(os.path.join(dir_name, file_name))]
        # print(f'{dir_name} has {len(file_names)} files and {len(dir_names)} directories.')
        # Delete the files.
        for each_directory in dir_names:
            print("Deleting files in " + each_directory + "...")
            for each_file in os.listdir(each_directory):
                if (
                    os.path.getmtime(each_directory + "/" + each_file)
                    < current_time - age * 86400
                ):
                    print(
                        f"Deleting file: {each_file} in {each_directory} because {os.path.getmtime(each_directory + '/' + each_file)} is older than {current_time - age * 8640} days."
                    )
                    os.chmod(each_directory + "/" + each_file, 0o777)
                    os.remove(each_directory + "/" + each_file)

            # Delete the directory.
            if os.rmdir(each_directory):
                os.chmod(each_directory, 0o777)
                dir_names.remove(each_directory)
                print(f"Deleting directory: {each_directory}.")
        do_delete(dir_name, age)
    except FileNotFoundError:
        print("The directory or file does not exist.")
    except RecursionError:
        #print("Maximum depth exceeded.") -- We don't need to know this. It's handled.
        if each_directory == "None":
            return True, None
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
        return True, None
    # If there are no more directories to delete, return False.
    elif not each_directory:
        return False, None
    return True, None


main()
print("Done.")

    """Code I'm saving for later.
    """
import ctypes
import sys

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


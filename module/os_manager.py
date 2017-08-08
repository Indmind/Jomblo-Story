import os

def clear():
    if os.name == "posix":
        # Unix/Linux/MacOS/BSD/etc
        os.system("clear")
    elif os.name in ("nt", "dos", "ce"):
        # DOS/Windows
        os.system("CLS")

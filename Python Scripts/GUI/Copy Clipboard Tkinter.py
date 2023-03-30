# This example will work on all OS including Android
# pip install tkinter
from tkinter import Tk

def clip():
    root = Tk()
    root.withdraw()
    clipboard = root.clipboard_get()
    return clipboard

def main():
    print(clip())

if __name__ == "__main__":
    main()

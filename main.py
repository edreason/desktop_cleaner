# Author: Ed Reason, 2022

import shutil
import sys

import tkinter as tk
import os
import time
import glob
from PIL import Image


# class TestSetup:


# Define file paths
desktop_dir = r"/Users/EdReason/Desktop/Test/"
target_dir = "TheShadowRealm/"
dst_dir = desktop_dir + target_dir
test_file_name = "beans.txt"


def file_move(src_path, dst_path, target_file):
    # Check if file exists in destination
    if os.path.exists(dst_path + target_file):
        # Split name and extension
        data = os.path.splitext(target_file)
        name = data[0]
        ext = data[1]
        # Add new name
        new_base = name + "_new" + ext
        # Construct full path
        new_name = os.path.join(dst_path, new_base)
        # Move file
        print(f"{target_file} exists in target directory! Renaming...")
        shutil.move(src_path + target_file, new_name)
        print(f"\nMoved {src_path}{target_file}\nDestination is {dst_path}{new_base}")
    else:
        shutil.move(src_path + target_file, dst_path + target_file)
        print(f"\nMoved {src_path}{target_file}\nDestination is {dst_path}{target_file}")


def test_setup(src_path, target_file):
    # Remove previously created files
    os.system(f"rm -rf {src_path}/*")
    time.sleep(2)
    # Create test files and directories
    os.mkdir(src_path + "/Beans")
    with open(f"{src_path}/{target_file}", 'w') as f:
        f.write("Create new test file!")
    with open(f"{src_path}bum{target_file}", 'w') as f:
        f.write("Hopefully I moved!")
    with open(f"{src_path}Beans/{target_file}", 'w') as f:
        f.write("Create new test file!")
    time.sleep(2)


# Window and text setup
root = tk.Tk()
message = tk.Label(root, text="Hello, World!")
message.pack()
root.title("Screenshot Cleanup")

# Window geometry setup
window_width = 1200
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
centre_x = int(screen_width/2 - window_width/2)
centre_y = int(screen_height/2 - window_height/2)
root.geometry(f"{window_width}x{window_height}+{centre_x}+{centre_y}")
root.resizable(False, False)

root.mainloop()


pattern = desktop_dir + "Screenshot*"
# test_setup(desktop_dir, test_file_name)
# file_move(desktop_dir, dst_dir, test_file_name)

# Move file with name starting with previously defined pattern
for file in glob.iglob(pattern, recursive=True):
    # Extract file name
    im = Image.open(file)
    im.show()
    response = input("Do you still need this screenshot? y/n\n")
    if response == "y":
        file_name = os.path.basename(file)
        file_move(desktop_dir, dst_dir, file_name)
        print("File moved to screenshots folder!")
    else:
        os.remove(file)
        print("File deleted!")

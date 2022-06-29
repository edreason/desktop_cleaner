# Author: Ed Reason, 2022

import shutil
import os
import time

# Define file paths
desktop_dir = r"/Users/EdReason/Desktop/Test/"
target_dir = "Beans/"
dst_dir = desktop_dir + target_dir
file_name = "beans.txt"


def file_move(src_path, dst_path, file):
    # Check if file exists in destination
    if os.path.exists(dst_path + file):
        # Split name and extension
        data = os.path.splitext(file)
        name = data[0]
        ext = data[1]
        # Add new name
        new_base = name + "_new" + ext
        # Construct full path
        new_name = os.path.join(dst_path, new_base)
        # Move file
        print(f"{file} exists in target directory! Renaming...")
        shutil.move(src_path + file, new_name)
        print(f"\nMoved {src_path}{file}\nDestination is {dst_path}{new_base}")
    else:
        shutil.move(src_path + file, dst_path + file)
        print(f"\nMoved {src_path}{file}\nDestination is {dst_path}{file}")


def test_setup(src_path, file):
    # Remove previously created files
    os.system(f"rm -rf {src_path}/*")
    time.sleep(2)
    # Create test files and directories
    os.mkdir(src_path + "/Beans")
    with open(f"{src_path}/{file}", 'w') as f:
        f.write("Create new test file!")
    with open(f"{src_path}Beans/{file}", 'w') as f:
        f.write("Create new test file!")
    time.sleep(2)


test_setup(desktop_dir, file_name)
file_move(desktop_dir, dst_dir, file_name)

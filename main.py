# Author: Ed Reason, 2022

import shutil

folder_path = r"/Users/EdReason/Desktop"

src_path = r"/Users/EdReason/Desktop/beans.txt"
dst_path = r"/Users/EdReason/Desktop/Beans/beans.txt"
shutil.move(src_path, dst_path)

# file detection là một cách để xác định loại file dựa trên nội dung của file đó. Để xác định loại file, chúng ta có thể sử dụng thư viện python-magic.

# # Cài đặt thư viện python-magic:
# pip install python-magic

# # Ví dụ về file detection:

import os

file_path = "text.txt"

if os.path.exists(file_path):
    print(f"File {file_path} exists")
    if os.path.isfile(file_path):
        print (f"File {file_path} is a file")
    elif os.path.isdir(file_path):
        print (f"File {file_path} is a directory")
    
else :
    print(f"File {file_path} does not exist")
    

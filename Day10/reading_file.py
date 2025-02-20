# reading_file là một cách để đọc dữ liệu từ file. Để đọc dữ liệu từ file, chúng ta có thể sử dụng hàm open với mode "r".

# # Ví dụ về reading file:

file_path = "C:/WorkSpace/Learning/Learning_Python_Zero_to_Hero/Day10/text.txt"
output_file = "output.txt"

with open(file_path, "r",encoding="utf-8") as file:
    data = file.read()
    print(data)  # In ra "Hello, world!"
    
# Trong ví dụ trên, chúng ta sử dụng hàm open để mở file text.txt với mode "r" và đọc dữ liệu từ file đó bằng cách sử dụng hàm read(). Sau đó, chúng ta in ra dữ liệu đó.

# # Có thể sử dụng hàm readlines để đọc từng dòng dữ liệu từ file:
# with open(output_file, "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line)  # In ra "\n", "This is a new line", "This is another new line"

import json 
import os

file_path = "C:/WorkSpace/Learning/Learning_Python_Zero_to_Hero/Day10/data.json"

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        print(data)  # In ra "{'name': 'Alice', 'age': 20, 'is_student': True}"
        
        
import csv
file_path = "C:/WorkSpace/Learning/Learning_Python_Zero_to_Hero/Day10/data.csv"

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)  # In ra "['name', 'age', 'is_student']", "['Alice', '20', 'True']"
            
        
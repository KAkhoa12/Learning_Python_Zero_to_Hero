# writing file là một cách để ghi dữ liệu vào file. Để ghi dữ liệu vào file, chúng ta có thể sử dụng hàm open với mode "w" hoặc "a".
# w là mode để ghi dữ liệu vào file. Nếu file không tồn tại, nó sẽ tạo ra file mới. Nếu file đã tồn tại, nó sẽ ghi đè lên nội dung của file đó.
# a là mode để ghi dữ liệu vào file. Nếu file không tồn tại, nó sẽ tạo ra file mới. Nếu file đã tồn tại, nó sẽ ghi dữ liệu vào cuối file đó.
# x là mode để tạo ra file mới và ghi dữ liệu vào file. Nếu file đã tồn tại, nó sẽ báo lỗi.

# # Ví dụ về writing file:

file_path = "text.txt"
output_file = "output.txt"
with open(file_path, "w") as file:
    file.write("Hello, world!")
    
with open(output_file, "a") as file:
    file.write("Hello, world!")  # Ghi dữ liệu vào cuối file output.txt
    
# Trong ví dụ trên, chúng ta sử dụng hàm open để mở file text.txt với mode "w" và ghi dữ liệu "Hello, world!" vào file đó. Sau đó, chúng ta sử dụng hàm open để mở file output.txt với mode "a" và ghi dữ liệu "Hello, world!" vào cuối file đó.

# # Có thể sử dụng hàm write để ghi nhiều dòng dữ liệu vào file:
with open(output_file, "a") as file:
    file.write("\n")
    file.write("This is a new line")  # Ghi dữ liệu vào cuối file output.txt    
    

# # Có thể sử dụng hàm writelines để ghi một list các dòng dữ liệu vào file:
lines = ["\n", "This is a new line", "This is another new line"]
with open(output_file, "a") as file:
    file.writelines(lines)  # Ghi dữ liệu vào cuối file output.txt
    
# Trong ví dụ trên, chúng ta sử dụng hàm write để ghi dữ liệu "\n" và "This is a new line" vào cuối file output.txt. Sau đó, chúng ta sử dụng hàm writelines để ghi list các dòng dữ liệu ["\n", "This is a new line", "This is another new line"] vào cuối file output.txt.

    
    
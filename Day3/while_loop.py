#  While loop là một cấu trúc lặp được sử dụng để lặp đi lặp lại một khối lệnh cho đến khi điều kiện lặp không còn đúng nữa.


# Ví dụ 1: In ra các số từ 1 đến 10
i = 1
while i <= 10:
    print(i)
    i += 1
    
name = input("Nhập tên của bạn: ")

while name == "":
    print("Tên không được để trống")
    name = input("Nhập tên của bạn: ")
print(f"Xin chào {name}")

    
    
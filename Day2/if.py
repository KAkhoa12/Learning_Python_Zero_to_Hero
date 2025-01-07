# if là câu lệnh điều kiện nếu đúng sẽ thực hiện hoặc ngược lại

# Ví dụ về if else và các câu lệnh cú pháp

# Ví dụ 1: Kiểm tra số dương, âm hoặc bằng 0
num = 3
if num > 0:
    print("Số dương")
elif num == 0:
    print("Bằng 0")
else:
    print("Số âm")

# Ví dụ 2: Kiểm tra tuổi để xác định độ tuổi
age = 20
if age < 18:
    print("Trẻ em")
elif 18 <= age < 65:
    print("Người lớn")
else:
    print("Người già")

# Ví dụ 3: Kiểm tra số chẵn hay lẻ
number = 4
if number % 2 == 0:
    print("Số chẵn")
else:
    print("Số lẻ")
    
    
operater = input("Nhập phép toán (+ - * /): ")
num1 = float(input(f"Nhập số thứ nhất: "))
num2 = float(input(f"Nhập số thứ hai: "))

if operater == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operater == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operater == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operater == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    # print("Phép toán không hợp lệ")
    pass # không làm gì cả (pass)

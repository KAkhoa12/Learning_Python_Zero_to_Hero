# user input input() là một hàm cho phép người dùng nhập dữ liệu từ bàn phím.

# Cú pháp:
name = input("Nhập tên: ")
age = int(input("Nhập tuổi: "))
age = age + 1

print(f"Xin chào {name}!")
print(f"Tôi: {age} tuổi!") 

# Bài tập 1: Nhập vào hai số và in ra tổng của chúng.
num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))
print(f"Tổng 2 số là {num1 + num2}")
# Bài tập 2: Nhập vào một chuỗi và in ra chuỗi đó viết hoa.
str_upercase = input("Nhập chuỗi cần viết hoa: ")
print(str_upercase.upper())


# Bài tập 3: Nhập vào một số và kiểm tra xem số đó có phải là số chẵn hay không.
number = int(input("Nhập số cần kiểm tra: "))
if number % 2 == 0:
    print("Đây là số chẵn")
else:
    print("Đây là số lẻ")

# Bài tập 4: Nhập vào chiều dài và chiều rộng của hình chữ nhật và tính diện tích của nó.

chieudai = float(input("Nhập chiều dài: "))
chieurong = float(input("Nhập chiều rộng: "))
dientich = chieudai * chieurong
print(f"Diện tích hình chữ nhật là {dientich}")

# Bài tập 5: Nhập vào một chuỗi và in ra số lượng ký tự trong chuỗi đó.
str_count = input("Nhập chuỗi cần đếm: ")
print(f"Số lượng ký tự trong chuỗi là {len(str_count)}")

#  Conditional Expression là một cách viết ngắn gọn của câu lệnh if else

# Ví dụ 1: Kiểm tra số dương, âm hoặc bằng 0

num = 3
result = "Số dương" if num > 0 else "Bằng 0" if num == 0 else "Số âm"

print(result)

# Ví dụ 2: Kiểm tra tuổi để xác định độ tuổi

age = 20
result = "Trẻ em" if age < 18 else "Người lớn" if 18 <= age < 65 else "Người già"

print(result)

# Ví dụ 3: Kiểm tra số chẵn hay lẻ

number = 4
result = "Số chẵn" if number % 2 == 0 else "Số lẻ"

print(result)
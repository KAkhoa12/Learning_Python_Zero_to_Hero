# match case statements là một cách để so sánh giá trị của biến với nhiều giá trị khác nhau mà không cần sử dụng nhiều câu lệnh if-elif-else. match case statements được giới thiệu từ Python 3.10.

# Cú pháp:
# match expression:
#     case value1:
#         # Xử lý khi biến bằng value1
#     case value2:
#         # Xử lý khi biến bằng value2
#     case _:
#         # Xử lý khi biến không bằng bất kỳ value nào

# Ví dụ:
# def check_number(number):
#     match number:
#         case 0:
#             print("Zero")
#         case 1:
#             print("One")
#         case 2:
#             print("Two")
#         case _:
#             print("Other")

# check_number(0)  # In ra "Zero"

# check_number(1)  # In ra "One"

# check_number(2)  # In ra "Two"

# check_number(3)  # In ra "Other"

# match case statements cũng hỗ trợ sử dụng if conditions trong mỗi case:

# Ví dụ:
# def check_number(number):
#     match number:
#         case 0:
#             print("Zero")
#         case 1:
#             print("One")
#         case 2:
#             print("Two")
#         case _ if number < 0:

#             print("Negative")
#         case _:  # Mặc định
#             print("Other")

# check_number(-1)  # In ra "Negative"


# exception handlling là một cách để xử lý các lỗi xảy ra trong quá trình thực thi chương trình. Khi một lỗi xảy ra, chương trình sẽ dừng lại và in ra thông báo lỗi. Để xử lý lỗi, chúng ta có thể sử dụng các câu lệnh try, except, else và finally.

# # Ví dụ về exception handling:

try:
    a = 1 / 0   # Lỗi ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero")
# Trong ví dụ trên, chúng ta sử dụng câu lệnh try để thực thi một đoạn code m
# a có thể

# # Có thể sử dụng nhiều except cho một câu lệnh try:
try:
    a = 1 / 0   # Lỗi ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero")
except ArithmeticError:
    print("Arithmetic error")
    
# # Có thể sử dụng else để thực thi một đoạn code khi không có lỗi xảy ra:
try:
    a = 1 / 1
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("No error")
    
# # Có thể sử dụng finally để thực thi một đoạn code sau khi thực thi câu lệnh try hoặc except:
try:
    a = 1 / 0   # Lỗi ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Done")
    
    
    
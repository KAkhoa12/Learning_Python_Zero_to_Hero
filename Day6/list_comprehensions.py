#  list comperhensions là một cách tạo ra một list mới từ một list đã có hoặc một iterable khác.

# Cú pháp:
# [expression for item in iterable if condition]

# Trong đó:
# - expression là biểu thức sẽ được thêm vào list mới.
# - item là biến lặp qua các phần tử của iterable.
# - iterable là một đối tượng có thể lặp qua.

# Ví dụ:
# fruits = ["apple", "banana", "cherry"]
# new_fruits = [fruit.upper() for fruit in fruits]

# print(new_fruits)  # In ra ["APPLE", "BANANA", "CHERRY"]

# # Sử dụng if condition
# numbers = [1, 2, 3, 4, 5]
# even_numbers = [number for number in numbers if number % 2 == 0]

# print(even_numbers)  # In ra [2, 4]

# # Sử dụng if else
# numbers = [1, 2, 3, 4, 5]
# new_numbers = [number * 2 if number % 2 == 0 else number / 2 for number in numbers]

# print(new_numbers)  # In ra [0.5, 4, 1.5, 8, 2.5]
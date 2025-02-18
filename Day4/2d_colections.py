# 2D Collections là các cấu trúc dữ liệu dùng để lưu trữ nhiều giá trị trong một biến, mỗi giá trị có thể là một cấu trúc dữ liệu khác như list, set, tuple, dictionary, ...

# Các cấu trúc dữ liệu 2D Collections:

# - List of lists: là một list chứa các list khác.
# - List of sets: là một list chứa các set khác.
# - List of tuples: là một list chứa các tuple khác.
# - List of dictionaries: là một list chứa các dictionary khác.

# Ví dụ: List of lists

# List of lists

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# In ra các phần tử của matrix
print("Matrix elements:")
for row in matrix:
    for number in row:
        print(number, end=" ")
    print()
    
# Ví dụ: List of sets

# List of sets

matrix = [{"apple", "banana", "cherry"}, {"red", "green", "blue"}, {"John", "Jane", "Alice"}]

# In ra các phần tử của matrix
print("\nMatrix elements:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# Ví dụ: List of tuples

# List of tuples

matrix = [("apple", "banana", "cherry"), ("red", "green", "blue"), ("John", "Jane", "Alice")]

# In ra các phần tử của matrix
print("\nMatrix elements:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# Ví dụ: List of dictionaries

# List of dictionaries

matrix = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}, {"name": "Alice", "age": 35}]
# In ra các phần tử của matrix

print("\nMatrix elements:")

for row in matrix:
    for key, value in row.items():
        print(key + ":", value, end=" ")
    print()


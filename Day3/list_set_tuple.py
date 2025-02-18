# List, set, tuple là các cấu trúc dữ liệu dùng để lưu trữ nhiều giá trị trong một biến.

# List: là một dãy các phần tử có thể thay đổi được, được đặt trong dấu ngoặc vuông [] và các phần tử cách nhau bởi dấu phẩy.
# Ví dụ:
numbers = [1, 2, 3, 4, 5]

# Set: là một tập hợp các phần tử không có thứ tự, không thể truy cập bằng chỉ số, không chứa các phần tử trùng lặp, được đặt trong dấu ngoặc nhọn {} và các phần tử cách nhau bởi dấu phẩy.
# Ví dụ:
colors = {"red", "green", "blue"}

# Tuple: là một dãy các phần tử không thể thay đổi được, được đặt trong dấu ngoặc tròn () và các phần tử cách nhau bởi dấu phẩy.
# Ví dụ:
fruits = ("apple", "banana", "cherry")

# Các phần tử trong list, set, tuple có thể là bất kỳ kiểu dữ liệu nào như số, chuỗi, list, set, tuple, dictionary, ...
# Ví dụ:

mixed = [1, "apple", {"name": "John", "age": 30}, (1, 2, 3)]

# Khi nào sử dụng list, set, tuple:
# - Sử dụng list khi bạn cần một dãy các phần tử có thứ tự và có thể thay đổi được.
# - Sử dụng set khi bạn cần một tập hợp các phần tử không có thứ tự và không chứa các phần tử trùng lặp.
# - Sử dụng tuple khi bạn cần một dãy các phần tử có thứ tự và không thể thay đổi được.
# Ví dụ in ra các phần tử của list, set, tuple:

# In ra các phần tử của list
print("List elements:")
for number in numbers:
    print(number)

# In ra các phần tử của set
print("\nSet elements:")
for color in colors:
    print(color)

# In ra các phần tử của tuple
print("\nTuple elements:")
for fruit in fruits:
    print(fruit)
    
mixed.reverse()
# print(mixed)
print(help(fruits))

new_list = []

new_list.append(1)
new_list.clear()
new_list = numbers.copy()
print(new_list)
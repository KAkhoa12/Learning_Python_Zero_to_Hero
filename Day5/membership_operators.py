# membership operators là các toán tử dùng để kiểm tra xem một giá trị có tồn tại trong một chuỗi, danh sách, hoặc bất kỳ cấu trúc dữ liệu nào khác không. Có hai toán tử membership: in và not in. in trả về True nếu giá trị tồn tại trong cấu trúc dữ liệu, ngược lại trả về False. not in trả về True nếu giá trị không tồn tại trong cấu trúc dữ liệu, ngược lại trả về False.

# Ví dụ 1: Kiểm tra xem một phần tử có tồn tại trong một danh sách hay không
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)  # True
print(6 in numbers)  # False

# Ví dụ 2: Kiểm tra xem một ký tự có tồn tại trong một chuỗi hay không
name = "Python"
print("y" in name)  # True
print("z" in name)  # False

# Ví dụ 3: Kiểm tra xem một phần tử có tồn tại trong một tuple hay không

fruits = ("apple", "banana", "cherry")
print("apple" in fruits)  # True
print("orange" in fruits)  # False

# Ví dụ 4: Kiểm tra xem một phần tử có tồn tại trong một dictionary hay không
person = {"name": "John", "age": 30, "city": "New York"}
print("name" in person)  # True

# Ví dụ 5: Kiểm tra xem một phần tử có tồn tại trong một set hay không
colors = {"red", "green", "blue"}
print("red" in colors)  # True
print("yellow" in colors)  # False

# Ví dụ 6: Kiểm tra xem một phần tử có tồn tại trong một file hay không
with open("file.txt", "r") as file:
    print("hello" in file)  # True
    print("world" in file)  # False

# Ví dụ 7: Kiểm tra xem một phần tử có tồn tại trong một range hay không
print(5 in range(10))  # True
print(15 in range(10))  # False 


# Ví dụ 8: Kiểm tra xem một phần tử có tồn tại trong một chuỗi số hay không
print("5" in "12345")  # True
# for loop là một cấu trúc lặp được sử dụng để lặp đi lặp lại một khối lệnh cho mỗi phần tử trong một dãy hoặc một chuỗi.

# Ví dụ 1: In ra các số từ 1 đến 10
for i in range(1, 11):
    print(i)
    
# Ví dụ 1: In ra các số từ 1 đến 10
for i in range(1, 11,2):
    print(i)
    
# Ví dụ 2: In ra các ký tự trong chuỗi
name = "Python"
for char in name:
    print(char)

# Ví dụ 3: In ra các phần tử trong list
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
    
# Ví dụ 4: In ra các phần tử trong tuple
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)

# Ví dụ 5: In ra các phần tử trong set
colors = {"red", "green", "blue"}
for color in colors:
    print(color)

# Ví dụ 6: In ra các phần tử trong dictionary

person = { "name": "John", "age": 30, "city": "New York"}
for key in person:
    print(key, person[key])
    print(key)
    
# Ví dụ 7: Sử dụng hàm enumerate để lấy cả chỉ số và giá trị
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(index, name)

# Ví dụ 8: Lặp qua hai danh sách cùng một lúc bằng zip
questions = ["name", "quest", "favorite color"]
answers = ["Lancelot", "the holy grail", "blue"]
for question, answer in zip(questions, answers):
    print(f"What is your {question}? It is {answer}.")
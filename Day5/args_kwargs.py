#  *args và **kwargs là cách để truyền một số lượng tham số không xác định vào hàm.

# *args là một tuple chứa các tham số không xác định.

# **kwargs là một dictionary chứa các tham số không xác định.

# Ví dụ:
def greet(*names):
    for name in names:
        print(f"Hello, {name}!")

greet("Alice", "Bob", "Charlie")  # In ra "Hello, Alice!", "Hello, Bob!", "Hello, Charlie!"

def greet(**names):
    print(names)
    for name, age in names.items():
        print(f"Hello, {name}! You are {age} years old.")

greet(Alice=20, Bob=25, Charlie=30)  # In ra "Hello, Alice! You are 20 years old.", "Hello, Bob! You are 25 years old.", "Hello, Charlie! You are 30 years old."

# Ví dụ kết hợp cả ba loại tham số:
def greet(*names, **ages):
    print(names)
    for name in names:
        print(f"Hello, {name}!")
    for name, age in ages.items():
        print(f"{name} is {age} years old.")
        
greet("Alice", "Bob", "Charlie", Alice=20, Bob=25, Charlie=30)  # In ra "Hello, Alice!", "Hello, Bob!", "Hello, Charlie!", "Alice is 20 years old.", "Bob is 25 years old.", "Charlie is 30 years old."

# iterables là một cách để lặp qua các phần tử của một đối tượng. Có nhiều loại đối tượng có thể được lặp qua, bao gồm list, tuple, dictionary, set, string, file, range, ...

# Ví dụ:

# Lặp qua một list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
# Lặp qua một tuple
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)

# Lặp qua một dictionary
fruits = {"apple": 1, "banana": 2, "cherry": 3}
for fruit in fruits:
    print(fruit)

# Lặp qua một set
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)
    
# Lặp qua một string
for char in "hello":
    print(char)
    
# Lặp qua một file
with open("file.txt", "r") as file:
    for line in file:
        print(line, end="")

# Lặp qua một range
for i in range(5):
    print(i)
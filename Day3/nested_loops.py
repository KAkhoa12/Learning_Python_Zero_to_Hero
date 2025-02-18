# Nestesd loops là một vòng lặp nằm bên trong một vòng lặp khác.

# Ví dụ 1: In ra các số từ 1 đến 10
for i in range(1, 11):
    for j in range(1, 11):
        print(i, j)
        
# Ví dụ 2: In ra các ký tự trong chuỗi
name = "Python"
for char in name:
    for char2 in name:
        print(char, char2)
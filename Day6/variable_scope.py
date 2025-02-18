# variable scope là một khái niệm để mô tả phạm vi sử dụng của biến trong chương trình. Có 2 loại variable scope chính trong Python: global scope và local scope.

# global scope: biến được khai báo ở ngoài tất cả các hàm, class, ... được coi là global scope. Biến global scope có thể được truy cập từ bất kỳ đâu trong chương trình.

# local scope: biến được khai báo trong một hàm, class, ... được coi là local scope. Biến local scope chỉ có thể được truy cập từ bên trong hàm, class, ... mà nó được khai báo.

# Ví dụ:
# x = 10  # global scope
# 
# def greet():
#     y = 20  # local scope
#     print(x)  # In ra 10
#     print(y)  # In ra 20

# greet()
# print(x)  # In ra 10
# print(y)  # Lỗi: NameError: name 'y' is not defined
# Trong ví dụ trên, x được khai báo ở ngoài hàm greet() nên x là global scope. y được khai báo trong hàm greet() nên y là local scope. Khi chúng ta gọi hàm greet(), chúng ta có thể truy cập được x từ bên trong hàm greet() nhưng không thể truy cập được y từ bên ngoài hàm greet().

# Để truy cập biến global scope từ bên trong hàm, chúng ta cần sử dụng từ khóa global.

# Ví dụ:
# x = 10  # global scope
#
# def greet():
#     global x
#     x = 20
#     print(x)  # In ra 20
#
# greet()
# print(x)  # In ra 20
# Trong ví dụ trên, chúng ta sử dụng từ khóa global để truy cập biến x ở global scope từ bên trong hàm greet().
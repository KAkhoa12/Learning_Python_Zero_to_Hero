# decorators là một cách để thay đổi hoặc mở rộng chức năng của một hàm hoặc một class mà không cần thay đổi code của hàm hoặc class đó. Để tạo một decorator, chúng ta sử dụng ký hiệu @ trước tên của decorator và đặt decorator đó trước hàm hoặc class mà chúng ta muốn thay đổi hoặc mở rộng chức năng.

# Ví dụ về decorator:
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args {args} and kwargs {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@debug
def add(a, b):
    return a + b

print(add(1, 2))  # In ra "Calling add with args (1, 2) and kwargs {}" và "3"
# Trong ví dụ trên, chúng ta định nghĩa một decorator debug để in ra tên của hàm và các arguments khi hàm đó được gọi. Chúng ta sử dụng decorator debug để thay đổi chức năng của hàm add. Khi chúng ta gọi hàm add với arguments 1 và 2, decorator debug sẽ in ra "Calling add with args (1, 2) and kwargs {}" và trả về kết quả của hàm add với arguments 1 và 2.

# # Có thể sử dụng nhiều decorator cho một hàm:
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args {args} and kwargs {kwargs}")
        return func(*args, **kwargs)
    return wrapper

def timer(func):
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Executed {func.__name__} in {end - start} seconds")
        return result
    return wrapper

@debug
@timer
def add(a, b):
    return a + b

print(add(1, 2))  # In ra "Calling wrapper with args (1, 2) and kwargs {}" và "Executed wrapper in 0.0 seconds" và "3"
# Trong ví dụ trên, chúng ta định nghĩa hai decorator debug và timer. Chúng ta sử dụng cả hai decorator để thay đổi chức năng của hàm add. Khi chúng ta gọi hàm add với arguments 1 và 2, decorator debug sẽ in ra "Calling add with args (1, 2) and kwargs {}" và decorator timer sẽ in ra "Executed add in 0.0 seconds" và trả về kết quả của hàm add với arguments 1 và 2.

# # Có thể sử dụng decorator cho một class:
def debug(cls):
    for name, value in vars(cls).items():
        if callable(value):
            setattr(cls, name, debug(value))
    return cls

@debug
class Math:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b
    
def debug_name(func):
    print(f"Calling {func.__name__}")
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args {args} and kwargs {kwargs}")
        return func(*args, **kwargs)
    return wrapper
    
@debug_name
def add(a, b):
    return a + b

print(add(1, 2))  # In ra "Calling add" và "Calling add with args (1, 2) and kwargs {}" và "3"





# multilthreading là một cách để thực thi nhiều tác vụ cùng một lúc. Để sử dụng multilthreading, chúng ta cần sử dụng thư viện threading.


# # # Ví dụ về multilthreading:

import threading

def print_numbers():
    for i in range(10):
        print(i)
        
def print_letters():
    for i in "abcdefghij":
        print(i)
        
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

# Trong ví dụ trên, chúng ta tạo hai thread t1 và t2 để thực thi hai hàm print_numbers và print_letters. Hàm print_numbers in ra các số từ 0 đến 9, trong khi hàm print_letters in ra các chữ cái từ a đến j. Khi chúng ta chạy chương trình, các số và chữ cái sẽ được in ra xen kẽ nhau.

# # # Có thể sử dụng tham số args để truyền arguments cho hàm:
import threading

def print_numbers(n):
    for i in range(n):
        print(i)
        
def print_letters(n):
    for i in range(n):
        print(i)
        
t1 = threading.Thread(target=print_numbers, args=(10,))

t2 = threading.Thread(target=print_letters, args=(10,))
t1.start()
t2.start()

t1.join()
t2.join()

# Trong ví dụ trên, chúng ta truyền arguments 10 cho cả hai hàm print_numbers và print_letters bằng cách sử dụng tham số args.

# # # Có thể sử dụng tham số kwargs để truyền keyword arguments cho hàm:

import threading

def print_numbers(n, end):
    for i in range(n):
        print(i, end=end)
        
def print_letters(n, end):
    for i in range(n):
        print(i, end=end)
        
t1 = threading.Thread(target=print_numbers, args=(10,), kwargs={"end": " "})

t2 = threading.Thread(target=print_letters, args=(10,), kwargs={"end": " "})
t1.start()
t2.start()

t1.join()
t2.join()

# Trong ví dụ trên, chúng ta truyền keyword argument "end" với giá trị " " cho cả hai hàm print_numbers và print_letters bằng cách sử dụng tham số kwargs.

# # # Có thể sử dụng tham số daemon để đặt thread thành daemon thread:

import threading

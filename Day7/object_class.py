# python object oriented programming là một phong cách lập trình, trong đó chương trình được chia thành các object. Mỗi object có các thuộc tính và phương thức riêng. Object có thể tương tác với nhau thông qua việc gọi phương thức của object khác.

# Ví dụ:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    
alice = Person("Alice", 20)
alice.greet()  # In ra "Hello, my name is Alice and I am 20 years old."

bob = Person("Bob", 25)
bob.greet()  # In ra "Hello, my name is Bob and I am 25 years old."

# Trong ví dụ trên, chúng ta định nghĩa một class Person với hai thuộc tính name và age. Phương thức __init__() được gọi khi một object mới được tạo. Phương thức greet() được sử dụng để in ra thông tin của object.

# Chúng ta tạo hai object alice và bob từ class Person và g
# reet() để in ra thông tin của mỗi object.

# Một số khái niệm cơ bản trong OOP:
# class: một class là một bản thiết kế để tạo ra các object. Một class bao gồm các
# thuộc tính (attributes) và phương thức (methods).
# object: một object là một thể hiện của một class. Mỗi object
# có các thuộc tính và phương thức riêng.
# attribute: một attribute là một biến được lưu trữ trong một object.
# method: một method là một hàm được định nghĩa trong một class.
# __init__(): phương thức __init__() được gọi khi một object mới được tạo.
# self: self là một biến đại diện cho object hiện tại.
# inheritance: inheritance là một tính chất cho phép một class kế thừa các thuộc
# tính và phương thức từ một class khác.
# encapsulation: encapsulation là một tính chất cho phép che dấu thông tin bên
# trong một class.
# polymorphism: polymorphism là một tính chất cho phép một phương thức có thể
# hoạt động với nhiều kiểu dữ liệu khác nhau.

# Ví dụ về inheritance:
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
    

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    
dog = Dog("Dog")
print(dog.speak())  # In ra "Dog says Woof!"
cat = Cat("Cat")
print(cat.speak())  # In ra "Cat says Meow!"
# Trong ví dụ trên, chúng ta định nghĩa một class Animal với một phương thức abstract speak(). Phương thức speak() được raise một NotImplementedError để báo lỗi nếu không có class con nào implement phương thức này.

# Chúng ta tạo hai class con Dog và Cat từ class Animal và implement phương thức speak() cho mỗi class con.

# Khi chúng ta gọi phương thức speak() của object dog và cat, chúng ta sẽ nhận được kết quả tương ứng "Dog says Woof!" và "Cat says Meow!".
# Ví dụ về encapsulation:
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        self._age = age
        
        
alice = Person("Alice", 20)
print(alice.get_name())  # In ra "Alice"
alice.set_name("Alice Smith")
print(alice.get_name())  # In ra "Alice Smith"
# Trong ví dụ trên, chúng ta định nghĩa một class Person với hai thuộc tính _name và _age. Chúng ta sử dụng getter và setter để truy cập và thay đổi giá trị của thuộc tính.

# Khi chúng ta tạo một object alice từ class Person, chúng ta có thể sử dụng getter và setter để truy cập và thay đổi giá trị của thuộc tính _name.

# Ví dụ về polymorphism:

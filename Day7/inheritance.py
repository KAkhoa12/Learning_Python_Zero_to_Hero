# inheritance là một tính chất cho phép một class có thể kế thừa các thuộc tính và phương thức từ một class khác.

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
        
# mutilple inheritance là một tính chất cho phép một class có thể kế thừa từ nhiều class khác.

# Ví dụ về multiple inheritance:
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class Flyable:
    def fly(self):
        return f"{self.name} can fly"
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    
class Bird(Animal, Flyable):
    def speak(self):
        return f"{self.name} says Chirp!"
    
dog = Dog("Dog")
print(dog.speak())  # In ra "Dog says Woof!"
cat = Cat("Cat")
print(cat.speak())  # In ra "Cat says Meow!"
bird = Bird("Bird")
print(bird.speak())  # In ra "Bird says Chirp!"
print(bird.fly())  # In ra "Bird can
# Trong ví dụ trên, chúng ta định nghĩa một class Animal với một phương thức abstract speak(). Phương thức speak() được raise một NotImplementedError để báo lỗi nếu không có class con nào implement phương thức này.
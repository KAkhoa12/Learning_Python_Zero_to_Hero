# super() là một hàm giúp chúng ta gọi phương thức của class cha mà không cần phải ghi tên class cha.

# Ví dụ về super():
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class Flyable:
    def fly(self):
        return f"{self.name} can fly"
    
class Bird(Animal, Flyable):
    def __init__(self, name):
        super().__init__(name)
        
    def speak(self):
        return f"{self.name} says Chirp!"
    
bird = Bird("Bird")
print(bird.speak())  # In ra "Bird says Chirp!"
print(bird.fly())  # In ra "Bird can
# Trong ví dụ trên, chúng ta định nghĩa một class Bird kế thừa từ class Animal và Flyable. Trong phương thức __init__() của class Bird, chúng ta gọi super().__init__(name) để gọi phương thức __init__() của class Animal mà không cần phải ghi tên class Animal.

# Khi chúng ta tạo một object bird từ class Bird, chúng ta có thể gọi phương thức speak() và fly() của object bird. 
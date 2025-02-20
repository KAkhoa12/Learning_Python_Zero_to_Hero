# class method là một phương thức thuộc về class chứ không phải object. Để tạo một class method, chúng ta sử dụng decorator @classmethod trước phương thức.

# ví dụ
class Person:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Person.count += 1
        
    @classmethod
    def total_count(cls):
        return cls.count
    
person1 = Person("Alice")
person2 = Person("Bob")
person3 = Person("Charlie")
print(Person.total_count())  # In ra 3
# Trong ví dụ trên, chúng ta định nghĩa một class Person với một class variable count và một class method total_count(). Phương thức total_count() trả về giá trị của class variable count.

# Khi chúng ta tạo ba object person1, person2 và person3 từ class Person, giá trị của class variable count sẽ tăng lên 3. Chúng ta gọi phương thức total_count() thông qua class Person để lấy giá trị của class variable count.

# Chúng ta cũng có thể gọi class method thông qua object nhưng không phải là cách sử dụng chính thống. Ví dụ:


class Person:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Person.count += 1
        
    @classmethod
    def total_count(cls):
        return cls.count
    
person1 = Person("Alice")
person2 = Person("Bob")
person3 = Person("Charlie")
print(person1.total_count())  # In ra 3
# Trong ví dụ trên, chúng ta gọi phương thức total_count() thông qua object person1. Kết quả sẽ không thay đổi so với cách gọi thông qua class Person.

# Một ứng dụng phổ biến của class method là tạo một class factory method. Class factory method là một phương thức trả về một object của class đó. Ví dụ:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def from_birth_year(cls, name, birth_year):
        print(cls)
        return cls(name, 2021 - birth_year)
    
person = Person.from_birth_year("Alice", 2000)
print(person.name)  # In ra "Alice"
print(person.age)  # In ra 21

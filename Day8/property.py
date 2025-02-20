# property là một cách để tạo ra các thuộc tính đặc biệt trong Python. Các thuộc tính này có thể được đọc, ghi và xóa giống như các thuộc tính thông thường, nhưng chúng ta có thể thực hiện các hành động nhất định khi chúng ta đọc, ghi hoặc xóa giá trị của thuộc tính đó.

# Ví dụ về property:
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    @property
    def diameter(self):
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2
        
    @diameter.deleter
    def diameter(self):
        del self.radius
    
c = Circle(5)

print(c.radius)  # In ra "5"
print(c.diameter)  # In ra "10"

c.diameter = 20
print(c.radius)  # In ra "10"
print(c.diameter)  # In ra "20"
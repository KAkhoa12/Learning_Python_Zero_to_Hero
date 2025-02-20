# magic method là một loại phương thức đặc biệt trong Python, được dùng để thực hiện các hành động nhất định khi chúng ta thực hiện các phép toán trên object. Ví dụ, khi chúng ta thực hiện phép cộng giữa hai object, Python sẽ gọi phương thức __add__() của object đầu tiên. Khi chúng ta thực hiện phép so sánh giữa hai object, Python sẽ gọi phương thức __eq__() của object đầu tiên.


# Ví dụ về magic method:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
v1 = Vector(1, 2)
v2 = Vector(2, 3)
print(v1 + v2)  # In ra "(3, 5)"
print(v1 == v2)  # In ra "False"
# Trong ví dụ trên, chúng ta định nghĩa một class Vector với hai thuộc tính x và y. Chúng ta override phương thức __add__() để thực hiện phép cộng giữa hai object Vector. Khi chúng ta thực hiện phép cộng giữa hai object v1 và v2, Python sẽ gọi phương thức __add__() của object v1 và truyền object v2 vào phương thức __add__(). Kết quả trả về của phương thức __add__() sẽ là object mới có thuộc tính x là tổng của x của hai object và thuộc tính y là tổng của y của hai object.

# __add__() là một magic method cho phép chúng ta thực hiện phép cộng giữa hai object Vector.
# __eq__() là một magic method cho phép chúng ta so sánh hai object Vector.
# __str__() là một magic method cho phép chúng ta convert object Vector thành một string.
# __lt__() là một magic method cho phép chúng ta so sánh hai object Vector với toán tử "<".
# __le__() là một magic method cho phép chúng ta so sánh hai object Vector với toán tử "<=".
# __gt__() là một magic method cho phép chúng ta so sánh hai object Vector với toán tử ">".
# __ge__() là một magic method cho phép chúng ta so sánh hai object Vector với toán tử ">=".
# __ne__() là một magic method cho phép chúng ta so sánh hai object Vector với toán tử "!=".
# __sub__() là một magic method cho phép chúng ta thực hiện phép trừ giữa hai object Vector.
# __mul__() là một magic method cho phép chúng ta thực hiện phép nhân giữa hai object Vector.
# __truediv__() là một magic method cho phép chúng ta thực hiện phép chia giữa hai object Vector.
# __floordiv__() là một magic method cho phép chúng ta thực hiện phép chia lấy phần nguyên giữa hai object Vector.
# __mod__() là một magic method cho phép chúng ta thực hiện phép chia lấy phần dư giữa hai object Vector.
# __pow__() là một magic method cho phép chúng ta thực hiện phép lũy thừa giữa hai object Vector.
# __and__() là một magic method cho phép chúng ta thực hiện phép AND giữa hai object Vector.
# __or__() là một magic method cho phép chúng ta thực hiện phép OR giữa hai object Vector.
# __xor__() là một magic method cho phép chúng ta thực hiện phép XOR giữa hai object Vector.
# __contains__() là một magic method cho phép chúng ta kiểm tra xem một object có tồn tại trong một object khác không.
# __len__() là một magic method cho phép chúng ta lấy độ dài của một object.
# __getitem__() là một magic method cho phép chúng ta lấy một phần tử từ một object.
# __setitem__() là một magic method cho phép chúng ta thay đổi một phần tử trong một object.
# __delitem__() là một magic method cho phép chúng ta xóa một phần tử trong một object.
# __iter__() là một magic method cho phép chúng ta lặp qua một object.


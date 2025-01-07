#  string method là các phương thức dùng để xử lý chuỗi


name = "Nguyễn Văn A"
print(name.upper()) # => NGUYỄN VĂN A
print(name.lower()) # => nguyễn văn a
print(name.title()) # => Nguyễn Văn A
print(name.capitalize()) # => Nguyễn văn a
print(name.swapcase()) # => nGUYỆN vĂN a
print(name.replace("A", "B")) # => Nguyễn Văn B
print(name.count("n")) # => 2
print(name.find("V")) # => 7
print(name.index("V")) # => 7
print(name.startswith("N")) # => False
print(name.endswith("A")) # => True
print(name.isalpha()) # => False
print(name.isdigit()) # => False
print(name.isalnum()) # => False
print(name.isspace()) # => False
print(name.islower()) # => False
print(name.isupper()) # => False
print(name.istitle()) # => True
print(name.split()) # => ['Nguyễn', 'Văn', 'A']
print(name.split("V")) # => ['Nguyễn ', 'ăn A']
print(name.strip()) # => Nguyễn Văn A
print(name.lstrip()) # => Nguyễn Văn A
print(name.rstrip()) # => Nguyễn Văn A
print(name.center(20)) # =>    Nguyễn Văn A
print(name.ljust(20)) # => Nguyễn Văn A
print(name.rjust(20)) # => Nguyễn Văn A
print(name.zfill(20)) # => 0Nguyễn Văn A
print(name.join("123")) # => 1Nguyễn Văn A2Nguyễn Văn A3


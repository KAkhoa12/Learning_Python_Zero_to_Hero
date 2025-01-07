import math as m

print(m.pi) # => 3.141592653589793
print(m.e) # => 2.718281828459045
print(m.sqrt(4)) # => 2.0
print(m.ceil(3.14)) # => 4
print(m.floor(3.14)) # => 3
print(m.pow(2, 3)) # => 8.0
print(m.log(10)) # => 2.302585092994046
print(m.log10(10)) # => 1.0
print(m.sin(m.pi/2)) # => 1.0
print(m.cos(m.pi)) # => -1.0
print(m.tan(m.pi/4)) # => 0.9999999999999999
print(m.degrees(m.pi)) # => 180.0

# Bài tập 1: Tính căn bậc hai của 16 và 25
print(f"Căn bậc 2 của 16 là",m.sqrt(16))
print(f"Căn bậc 2 của 25 là",m.sqrt(25))

# Bài tập 2: Tính giá trị của 5 mũ 3 và 2 mũ 8
print(f"5 mũ 3 là {m.pow(5,3)}")
print(f"2 mũ 8 là {m.pow(2,8)}")
# Bài tập 3: Tính logarit cơ số e của 20 và logarit cơ số 10 của 1000
print(f"logarit cơ số e của 20 là {m.log(20)}")
print(f"logarit cơ số 10 của 1000 là {m.log10(1000)}")
# Bài tập 4: Tính sin, cos và tan của góc 45 độ (chuyển đổi từ độ sang radian trước khi tính)
print(f"sin của góc 45 độ là {m.sin(m.radians(45))}")
print(f"cos của góc 45 độ là {m.cos(m.radians(45))}")
print(f"tan của góc 45 độ là {m.tan(m.radians(45))}")

# Bài tập 5: Tính giá trị của pi và e, sau đó làm tròn lên và làm tròn xuống giá trị của chúng
print(f"Giá trị của pi là {m.pi}")
print(f"Giá trị của e là {m.e}")
print(f"Làm tròn lên giá trị của pi là {m.ceil(m.pi)}")
print(f"Làm tròn xuống giá trị của pi là {m.floor(m.pi)}")
print(f"Làm tròn lên giá trị của e là {m.ceil(m.e)}")
print(f"Làm tròn xuống giá trị của e là {m.floor(m.e)}")
# Bài tập 6: Chuyển đổi 90 độ và 360 độ sang radian
print(f"90 độ sang radian là {m.radians(90)}")
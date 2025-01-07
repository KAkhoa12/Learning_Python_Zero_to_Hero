# format specifiers là một chuỗi định dạng được sử dụng để định dạng chuỗi, số nguyên, số thực, ...
price = 49
price1 = 50.99
txt = "The price is {:d} dollars"
print(txt.format(price))

txt1 = "The price is {:.2f} dollars"
print(txt1.format(price))

txt2 = "The price is {:.2f} dollars"
print(txt2.format(price1))

txt3 = "The price is {:f} dollars"
print(txt3.format(price1))
# Định dạng giá trị dưới dạng số thập lục phân (hexadecimal)
txt4 = "The price is {:x} dollars"
print(txt4.format(price))

# Định dạng giá trị dưới dạng số bát phân (octal)
txt5 = "The price is {:o} dollars"
print(txt5.format(price))

# Cách dãn hàng giữa chuỗi và giá trị
txt6 = f"The price is {price:10} dollars"
print(txt6)

txt7 = f"The price is {price:10d} dollars"
print(txt7)

txt8 = f"The price is {price1:*>10.2f} dollars"
print(txt8)

# Định dạng giá trị dưới dạng số nhị phân (binary)
txt9 = "The price is {:b} dollars"
print(txt9.format(price))

# Định dạng giá trị dưới dạng phần trăm
txt10 = "The price is {:.0%} of the total"
percentage = 0.25
print(txt10.format(percentage))

# Định dạng giá trị với dấu phẩy phân tách hàng nghìn
txt11 = "The price is {:,} dollars"
large_number = 1000000
print(txt11.format(large_number))

# Định dạng giá trị với dấu cộng/ trừ
txt12 = "The price change is {:+} dollars"
price_change = 5
print(txt12.format(price_change))

# Định dạng giá trị với căn giữa
txt13 = "The price is {:^10} dollars"
print(txt13.format(price))
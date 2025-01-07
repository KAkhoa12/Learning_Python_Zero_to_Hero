# String indexing là cách truy cập vào từng ký tự trong chuỗi thông qua chỉ số index

# [start:stop:step]
# start: chỉ số bắt đầu
# stop: chỉ số kết thúc
# step: bước nhảy
# Ví dụ về string indexing
name = "Nguyễn Văn A"
print(name[0]) # => N
print(name[1]) # => g
print(name[-1]) # => A
print(name[-2]) # =>
print(name[0:6]) # => Nguyễn
print(name[:6]) # => Nguyễn
print(name[7:]) # => Văn A
print(name[7:10]) # => Văn
print(name[-1:-4]) # =>
print(name[-4:-1]) # => Văn
print(name[0:10:2]) # => NynVn
print(name[::2]) # => NynVn
print(name[::-1]) # => A năV nệuyN
print(name[::-2]) # => AnVnệy
print(name[0:10:-1]) # =>
print(name[10:0:-1]) # => A nV nệuy
print(name[10::-1]) # => A nV nệuyN
print(name[:10:-1]) # => A
print(name[10:0:-2]) # => A Vn
print(name[10::-2]) # => A Vn

number_string ="1234-5678-9876-5432"
print(number_string[5]) # => 5
print(number_string[5:10]) # => 5678-
print(number_string[5:10:2]) # => 57-
print(number_string[5:10:-1]) # => 
print(number_string[::-1]) # => 2345-6789-8765-4321
print(number_string[10:5:-1]) # => 9-876
print(number_string[10:5:-2]) # => 986
print(number_string[10:5:-3]) # => 986
print(number_string[10:])
print(number_string[:10])

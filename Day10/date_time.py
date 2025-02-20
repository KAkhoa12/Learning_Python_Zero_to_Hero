# date time là một thư viện trong python dùng để xử lý thời gian và ngày tháng. Để sử dụng thư viện date time, chúng ta cần import thư viện date time bằng cách sử dụng lệnh import datetime.


# # # Ví dụ về date time:
import datetime

# # # Lấy ngày và giờ hiện tại:
now = datetime.datetime.now()
print(now)

# # # Lấy ngày hiện tại:
today = datetime.date.today()
print(today)

# # # Lấy thời gian hiện tại:
time = datetime.datetime.time(now)
print(time)

# # # Lấy ngày và giờ theo định dạng:
now = datetime.datetime.now()

# # # Định dạng ngày và giờ theo chuỗi:
formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
print(formatted_date)

# # # Chuyển đổi chuỗi thành ngày:
date_string = "2021-01-01"
date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
print(date)

# # # Tính toán thời gian:
now = datetime.datetime.now()
delta = datetime.timedelta(days=1)
tomorrow = now + delta
print(tomorrow)

# # # So sánh thời gian:
now = datetime.datetime.now()
tomorrow = now + datetime.timedelta(days=1)

if now < tomorrow:
    print("Tomorrow is greater than now")
else:
    print("Now is greater than tomorrow")
    
# # # Tính toán khoảng cách giữa hai thời gian:
now = datetime.datetime.now()
tomorrow = now + datetime.timedelta(days=1)

delta = tomorrow - now
print(delta.days)

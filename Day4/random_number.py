# Random 
import random
print(random.randint(1, 10))  # In ra một số nguyên ngẫu nhiên từ 1 đến 10
print(random.random())  # In ra một số thực ngẫu nhiên từ 0.0 đến 1.0
print(random.choice([1, 2, 3, 4, 5]))  # Chọn ngẫu nhiên một phần tử từ danh sách
print(random.choices([1, 2, 3, 4, 5], k=2))  # Chọn ngẫu nhiên k phần tử từ danh sách, cho phép trùng lặp
print(random.sample([1, 2, 3, 4, 5], k=2))  # Chọn ngẫu nhiên k phần tử từ danh sách, không trùng lặp
print(random.shuffle([1, 2, 3, 4, 5]))  # Trộn ngẫu nhiên các phần tử trong danh sách
print(random.seed(4))  # Đặt hạt giống cho bộ sinh số ngẫu nhiên
print(random.getstate())  # Lấy trạng thái hiện tại của bộ sinh số ngẫu nhiên
print(random.setstate(random.getstate()))  # Đặt trạng thái cho bộ sinh số ngẫu nhiên
print(random.getstate())  # Lấy trạng thái hiện tại của bộ sinh số ngẫu nhiên
print(random.getrandbits(4))  # In ra một số nguyên ngẫu nhiên với 4 bit
print(random.uniform(1, 10))  # In ra một số thực ngẫu nhiên từ 1.0 đến 10.0
print(random.triangular(1, 10, 5))  # In ra một số thực ngẫu nhiên theo phân phối tam giác
print(random.betavariate(1, 10))  # In ra một số thực ngẫu nhiên theo phân phối beta
print(random.expovariate(1))  # In ra một số thực ngẫu nhiên theo phân phối mũ
print(random.gammavariate(1, 10))  # In ra một số thực ngẫu nhiên theo phân phối gamma
print(random.gauss(1, 10))  # In ra một số thực ngẫu nhiên theo phân phối Gaussian (chuẩn)
print(random.lognormvariate(1, 10))  # In ra một số thực ngẫu nhiên theo phân phối log-normal
print(random.normalvariate(1, 10))  # In ra một số thực ngẫu nhiên theo phân phối chuẩn
print(random.vonmisesvariate(1, 10))  # In ra một số thực ngẫu nhiên theo phân phối von Mises
print(random.paretovariate(1))  # In ra một số thực ngẫu nhiên theo phân phối Pareto
print(random.weibullvariate(1, 10))  # In ra một số thực ngẫu nhiên theo phân phối Weibull



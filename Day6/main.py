# __main__ là một module đặc biệt trong Python, nó chứa code chính của chương trình. Khi chạy một file Python, Python sẽ tự động tạo một module __main__ và chạy code trong đó.

# Ví dụ:
def main():
    print("Hello, Python!")
    
if __name__ == "__main__":
    main()
# Trong ví dụ trên, chúng ta định nghĩa một hàm main() và kiểm tra xem module hiện tại có phải là module __main__ không. Nếu đúng, chúng ta gọi hàm main(). Khi chúng ta chạy file Python này, chương trình sẽ in ra "Hello, Python!".
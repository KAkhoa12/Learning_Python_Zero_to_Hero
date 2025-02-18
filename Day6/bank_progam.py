from module_bank import *

def menu():
    print("1. Xem so du")
    print("2. nap tien")
    print("3. rut tien")
    print("4. thoat")

def main():
    is_exits = False
    while not is_exits:
        menu()
        choice = input("chon chuc nang: ")
        match choice:
            case "1":
                print(xem_so_du())
            case "2":
                so_tien_nap = int(input("Nhap so tien nap: "))
                nap_tien(so_tien_nap)
            case "3":
                so_tien_rut = int(input("Nhap so tien rut: "))
                if not rut_tien(so_tien_rut):
                    print("So tien ban rut lon hon so du")
                else:
                    print("Rut tien thanh cong")
            case "4":
                is_exits = True
            case _:
                print("Chức năng không tồn tại")
                
if __name__ == "__main__":
    main()
                
                
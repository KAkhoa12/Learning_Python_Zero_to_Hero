import random


list_of_type = [
    {
        0:"keo"
    },
    {
        1:"bua"
    },
    {
        2:"bao"
    }
]

continue_type = True

while continue_type:
    random_num = random.randint(0,2)
    
    type_user = int(input("Chon 0: Keo, 1: Bua, 2: Bao: "))
    
    while type_user not in [0,1,2]:
        type_user = int(input("Chọn sai rồi vui lòng! Chon 0: Keo, 1: Bua, 2: Bao: "))
    
    print(f"Bạn chọn {list_of_type[type_user][type_user]}")
    print(f"Máy chọn {list_of_type[random_num][random_num]}")
    
    if type_user == random_num:
        print("Hòa")
    elif type_user == 0 and random_num == 1:
        print("Thua")
    elif type_user == 1 and random_num == 2:
        print("Thua")
    elif type_user == 2 and random_num == 0:
        print("Thua")
    else:
        print("Thắng")
    

item = {
    "money": 1000000,
    "name": "Duc",
    "age": 20
}

def xem_so_du ():
    return item["money"]


def rut_tien (so_tien):
    if so_tien <= item["money"]:
        item["money"] -= so_tien
        return True
    else:
        return False

def nap_tien (so_tien):
    item["money"] += so_tien
    return True

def chuyen_tien (so_tien, nguoi_nhan):
    if so_tien <= item["money"]:
        item["money"] -= so_tien
        nguoi_nhan["money"] += so_tien
        return True
    else:
        return False
    
if __name__ == "__main__":
    pass
    
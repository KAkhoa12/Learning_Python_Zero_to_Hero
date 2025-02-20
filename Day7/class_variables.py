# class variables là các biến được chia sẻ giữa tất cả các instance của một class. Để tạo một class variable, chúng ta đặt biến đó ở ngoài tất cả các phương thức trong class và trước tất cả các phương thức trong class.
import random 
# Ví dụ về class variables:
class SlotMachine:
    symbols = ["🍒", "🍊", "🍋", "🍉", "🍇", "🍓"]
    
    def __init__(self):
        self.score = 0
        
    def spin(self):
        result = [random.choice(SlotMachine.symbols) for _ in range(3)]
        print(result)
        if result[0] == result[1] == result[2]:
            self.score += 10
        elif result[0] == result[1] or result[0] == result[2] or result[1] == result[2]:
            self.score += 5
        else:
            self.score -= 1
        return self.score
    
slot_machine = SlotMachine()
print(slot_machine.spin())
print(slot_machine.spin())
print(slot_machine.spin())
print(slot_machine.symbols)
# Trong ví dụ trên, chúng ta định nghĩa một class SlotMachine


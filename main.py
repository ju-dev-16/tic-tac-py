import time

class Table: 
    def __init__(self):
        self.table = [1, 2, 3,
                      4, 5, 6, 
                      7, 8, 9]   
    
    def get_table(self):
        print(
              f"{str(self.table[0])} | {str(self.table[1])} | {str(self.table[2])}\n" 
              f"{str(self.table[3])} | {str(self.table[4])} | {str(self.table[5])}\n"
              f"{str(self.table[6])} | {str(self.table[7])} | {str(self.table[8])}\n"
            )
        
    def update(self, choose):
        for i in self.table:
            if i == choose - 1:
                self.table[choose - 1] = current_player.get_symbol()
                     
table = Table()

class Player:
    def __init__(self):
        self.turn = False
        self.symbol = "❌"
        
    def get_symbol(self):
        return self.symbol
    
    def get_turn(self):
        return self.turn
    
    def set_turn(self):
        if self.turn is False:
            self.turn = True
            self.symbol = "⭕"
        elif self.turn is True:
            self.turn = False
            self.symbol = "❌"

current_player = Player()

def choose_number():
    choose = int(input("Wähle eine Zahl von 1-9: "))
    table.update(choose)

def repeat_process():
    while True:
        if current_player.get_turn() is False:
            time.sleep(0.25)
            print("\n❌ ist am Zug.\n")
            time.sleep(0.25)
        else:
            time.sleep(0.25)
            print("\n ⭕ ist am Zug.\n")
            time.sleep(0.25)
            
        choose_number()
        table.get_table()
        current_player.set_turn()
    
if __name__ == "__main__":
    repeat_process()

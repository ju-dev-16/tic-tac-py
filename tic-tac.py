from time import sleep

class Table: 
    def __init__(self):
        self.table = [1, 2, 3,
                      4, 5, 6, 
                      7, 8, 9]   
    
    def get_table(self):
        print(
              f"\n{str(self.table[0])} | {str(self.table[1])} | {str(self.table[2])}\n" 
              f"{str(self.table[3])} | {str(self.table[4])} | {str(self.table[5])}\n"
              f"{str(self.table[6])} | {str(self.table[7])} | {str(self.table[8])}"
            )
        
    def update(self, choose):
        for i in self.table:
            if self.table.index(i) == choose - 1:
                if self.table[choose - 1] == "❌" or self.table[choose - 1] == "⭕":
                    print("\n⚠ Du kannst keine Felder überschreiben!\nAls Strafe setzt du für diese Runde aus🙂")
                    break
                else:
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
        if self.get_turn() is False:
            self.turn = True
            self.symbol = "⭕"
        elif self.get_turn():
            self.turn = False
            self.symbol = "❌"
        
current_player = Player()

def choose_number():
    choose = int(input("Wähle eine Zahl von 1-9: "))
    table.update(choose)

def repeat_process():
    while True:
        if current_player.get_turn() is False:
            sleep(0.5)
            print("\n❌ ist am Zug.\n")
            sleep(0.5)
        else:
            sleep(0.5)
            print("\n⭕ ist am Zug.\n")
            sleep(0.5)
            
        choose_number()
        current_player.set_turn()
        table.get_table()
    
if __name__ == "__main__":
    repeat_process()

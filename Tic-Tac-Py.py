from time import sleep

class Table: 
    def __init__(self):
        self.table = [1, 2, 3, 4, 5, 6, 7, 8, 9]   
    
    def get_table(self):
        print(
              f"\n{str(self.table[0])} | {str(self.table[1])} | {str(self.table[2])}\n" 
              f"{str(self.table[3])} | {str(self.table[4])} | {str(self.table[5])}\n"
              f"{str(self.table[6])} | {str(self.table[7])} | {str(self.table[8])}"
            )
        
    def update(self, choose):
        for i in self.table:
            if self.table.index(i) == choose - 1:
                if self.table[choose - 1] == "X" or self.table[choose - 1] == "O":
                    print("\nDu kannst keine Felder überschreiben!\nAls Strafe setzt du für diese Runde aus :)")
                    break
                else: self.table[choose - 1] = current_player.get_symbol()
                    
    def check_row(self):
        if self.table[0] == current_player.get_symbol() and self.table[1] == current_player.get_symbol() and self.table[2] == current_player.get_symbol() or self.table[3] == current_player.get_symbol() and self.table[4] == current_player.get_symbol() and self.table[5] == current_player.get_symbol() or self.table[6] == current_player.get_symbol() and self.table[7] == current_player.get_symbol() and self.table[8] == current_player.get_symbol():
            print("\nWir haben einen Gewinner!")
            return True
    
    def check_split(self):
        if self.table[0] == current_player.get_symbol() and self.table[3] == current_player.get_symbol() and self.table[6] == current_player.get_symbol() or self.table[1] == current_player.get_symbol() and self.table[4] == current_player.get_symbol() and self.table[7] == current_player.get_symbol() or self.table[2] == current_player.get_symbol() and self.table[5] == current_player.get_symbol() and self.table[8] == current_player.get_symbol():
            print("\nWir haben einen Gewinner!")
            return True
    
    def check_quer(self):
        if self.table[0] == current_player.get_symbol() and self.table[4] == current_player.get_symbol() and self.table[8] == current_player.get_symbol() or self.table[6] == current_player.get_symbol() and self.table[4] == current_player.get_symbol() and self.table[2] == current_player.get_symbol():
            print("\nWir haben einen Gewinner!")
            return True
       
table = Table()

class Player:
    def __init__(self):
        self.turn = False
        self.symbol = "X"
        
    def get_symbol(self):
        return self.symbol
    
    def get_turn(self):
        return self.turn
    
    def set_turn(self):
        if self.get_turn() is False:
            self.turn = True
            self.symbol = "O"
        elif self.get_turn():
            self.turn = False
            self.symbol = "X"
        
current_player = Player()

def choose_number():
    choose = int(input("Wähle eine Zahl von 1-9: ")) 
    table.update(choose)

def game_loop():
    while True:
        if current_player.get_turn() is False:
            sleep(0.5)
            print("\nX ist am Zug.\n")
            sleep(0.5)
        else:
            sleep(0.5)
            print("\nO ist am Zug.\n")
            sleep(0.5)
            
        choose_number()
        
        if table.check_row() or table.check_quer() or table.check_split():
            sleep(0.5) 
            table.get_table()
            print("")
            break
        elif (table.table[0] == "X" or table.table[0] == "O") and (table.table[1] == "X" or table.table[1] == "O") and (table.table[2] == "X" or table.table[2] == "O") and (table.table[3] == "X" or table.table[3] == "O") and (table.table[4] == "X" or table.table[4] == "O") and (table.table[5] == "X" or table.table[5] == "O") and (table.table[6] == "X" or table.table[6] == "O") and (table.table[7] == "X" or table.table[7] == "O") and (table.table[8] == "X" or table.table[8] == "O"):
            sleep(0.5) 
            print("\nUnentschieden!!!")
            table.get_table()
            print("")
            break
            
        current_player.set_turn()
        table.get_table()
    
if __name__ == "__main__": game_loop()

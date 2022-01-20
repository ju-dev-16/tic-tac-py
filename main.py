import time

from table import table
from player import current_player

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
        table.check_field()
        table.get_table()
        current_player.set_turn()
    
if __name__ == "__main__":
    repeat_process()

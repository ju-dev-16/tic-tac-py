from player import current_player

class Table: 
    def __init__(self):
        self.table = [1, 2, 3,
                      4, 5, 6, 
                      7, 8, 9]   
    
    def get_table(self):
        print(
              " " + str(self.table[0]) + " | " + str(self.table[1]) + " | " + str(self.table[2]) + " \n" 
              " " + str(self.table[3]) + " | " + str(self.table[4]) + " | " + str(self.table[5]) + " \n" 
              " " + str(self.table[6]) + " | " + str(self.table[7]) + " | " + str(self.table[8]) + " \n"
            )
        
    def update(self, choose):
        for i in self.table:
            if i == choose - 1:
                self.table[choose - 1] = current_player.get_symbol()
                     
table = Table()

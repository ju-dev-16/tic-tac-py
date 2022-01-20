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

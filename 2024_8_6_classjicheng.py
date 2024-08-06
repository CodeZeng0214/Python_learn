class Drawer:
    def __init__(self,name,draw):
        self.name = name
        self.draw = draw
    
    def print_info(self):
        print(f"{self.name}的画作是{self.draw}")

class NowDrawer(Drawer):
    def __init__(self, name, draw,first):
        super().__init__(name, draw)
        self.first = first
    
    def print_time(self):
        print(f"{self.name}的{self.draw}首次出现在{self.first}")
        
kusanagi = NowDrawer("草薙直哉", "火水", "樱之刻")
kusanagi.print_info()
kusanagi.print_time()
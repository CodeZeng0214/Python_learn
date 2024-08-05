class Mahoushoujyo:
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def HerHope(self,hope):
        self.hope = hope
        print(self.name + '的愿望是' + hope)
    
himeori = Mahoushoujyo('姬织','purple')
chikazu = Mahoushoujyo('千和','green')
print(himeori.name + '的代表色是' + himeori.color)
print(chikazu.name + '的代表色是' + chikazu.color)

print(himeori.HerHope('让重要之人重回世间'))
print(chikazu.HerHope('与大雅共度余生'))
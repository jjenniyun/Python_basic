class Unit:
    def __init__(self):
        print("Unit 생성자")

class Fly:
    def __init__(self):
        print("fly 생성자")
        
class FlyUnit(Fly, Unit): # 순서 상 
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Fly.__init__(self)
        
drop = FlyUnit()
# 일반 유닛
class Unit: # 부모 클래스
    def __init__(self, name, hp, speed):
        self.name = name # 멤버변수
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
        
# 공격 유닛
class AttackUnit(Unit): # 상속
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1}방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
        
# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)
        
    def stim(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))
            
# 탱크
class Tank(AttackUnit):
    seize = False # 시즈모드 개발여부
    
    def __init__(self):
        AttackUnit.__init__(self,"탱크", 150,1,35)
        self.seize = False
        
    def set_seize(self):
        if Tank.seize == False:
            return
    
    # 현재 시즈모드가 아닐 때 
    
class Fly:
    def __init__(self, fly_speed):
        self.fly_speed = fly_speed
        
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.fly_speed))
    
# 공중 공격 유닛 클래스
class FlyAttackUnit(AttackUnit, Fly):
    def __init__(self, name, hp, damage, fly_speed):
        AttackUnit.__init__(self, name, hp,0, damage) # 스피드 0
        Fly.__init__(self, fly_speed)
        
    def move(self, location): # 재정의
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
        
# 레이스        
class wra(FlyAttackUnit):
    def __init__(self):
        FlyAttackUnit.__init__("레이스",80,20,5)
        self.clocked = False # 클로킹  모드(해제 상태)
        
    def clocking(self):
        if self.clocked == True:
            print("{0} 클로킹 모드 시작")
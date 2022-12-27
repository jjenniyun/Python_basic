# 클래스

name = "마린" # 유닛의 이름
hp = 40
damage = 5 # 유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp,tank2_damage))


def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))
    
attack(name,"1시",damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

# 일반 유닛
class Unit: # 부모 클래스
    def __init__(self, name, hp, speed):
        self.name = name # 멤버변수
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
# mar1 = Unit("마린",40,5) # 인스턴스
# mar2 = Unit("마린",40,5)
# tank = Unit("탱크", 150,35)
# mar3 = Unit("마린",40) # init함수에 정의된 객체만큼 적어야 함 # 오류
# 
# wra1 = Unit("레이스",80,5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wra1.name, wra1.damage))
# 
# wra2 = Unit("빼앗은 레이스",80,5)
# wra2.clocking = True
# 
# if wra2.clocking == True:
    # print("{0} 는 현재 클로킹 상태입니다.".format(wra2.name))

# 메소드
# 공격 유닛
class AttackUnit(Unit): # 상속
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1}방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
            
# fire1 = AttackUnit("파이어뱃",50,16)
# fire1.attack("5시")
# 공격 2번 받는 다고 가정
# fire1.damaged(25)
# fire1.damaged(25)
class Fly:
    def __init__(self, fly_speed):
        self.fly_speed = fly_speed
        
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.fly_speed))
        
class FlyAttackUnit(AttackUnit, Fly): # 다중 상속
    def __init__(self, name, hp, damage, fly_speed):
        AttackUnit.__init__(self, name, hp,0, damage) # 스피드 0
        Fly.__init__(self, fly_speed)
        
    def move(self, location): # 재정의
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
# val = FlyAttackUnit("발키리", 200, 6,5)
# val.fly(val.name, "3시")

# vul = AttackUnit("벌쳐",80,10,20)
# bat = FlyAttackUnit("배틀크루저",500,25,3)
# 
# vul.move("11시")
# bat.fly(bat.name, "9시")
# bat.move("9시")

class buildUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location =location
# supply = buildUnit("서플라이 디폿",500,"7시")
# 
# def game_start():
    # print("[알림] 새로운 게임을 시작합니다")
    # 
# def game_over():
    # pass
# 
# game_start()
# game_over()


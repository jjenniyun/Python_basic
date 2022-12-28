# 모듈(함수 정의나 클래스 파일 담고 있는 것)
import theater_module

# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조할인 영화 보러 갔을 때
# theater_module.price_solder(5) # 5명의 구인이 영화 보러 갔을 때

# import theater_module as mv # mv로 호출
# mv.price_solder(5)
# mv.price(3)
# mv.price_morning(4)

# from theater_module import *
# price(3)
# price_morning(4)
# price_solder(5)

# from theater_module import price, price_morning
# price(5)
# price_morning(6)

from theater_module import price_solder as price # as로 해서 별칭 사용
price(5)

# 패키지(모듈의 집합)
# import travel.thai # 모듈이나 패키지만 가능
# trip_to = travel.thai.ThaiPackage() # 패키지의 클래스 
# trip_to.detail()

# from travel.thai import ThaiPackage
# trip_to = ThaiPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from travel import * # 공개범위 설정 필요
trip_to = thai.ThaiPackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
#print(inspect.getfile(thai))
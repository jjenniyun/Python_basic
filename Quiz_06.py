# 표준 체중을 구하는 프로그램 작성
# 표준 체중 : 각 개인의 키에 적당한 체중

# 성별) 남: 키*키*22/ 여: 키*키*21
# 조건1 표준체중 함수명: std_weight 전달값 키(heigth) 성별(gender)
# 조건2 표준체중 소수점 둘째자리까지 표시

# 출력예제)
# 키 175cm 남자의 표준 체중은 67.38kg입니다

def std_weight(height, gender):
    if gender == "남자":
        return height * height *22
    else:
        return height*height*21
    
height = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height /100, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))
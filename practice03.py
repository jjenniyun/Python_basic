sentence ='나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고, 
파이썬은 쉬워요
"""
print(sentence3)

# 슬라이싱
jumin = "990120-1234567"

print("성별 : "+jumin[7])
print("연 : "+jumin[0:2])
print("월 : "+jumin[2:4])
print("일 "+jumin[4:6])

print("생년월일 : "+jumin[:6]) # [0:6]
print("뒤 7자리 : "+jumin[7:]) # [7:14]
print("뒤 7자리(뒤에서부터) : "+jumin[-7:])

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java")) # 문장안의 값 바꾸기

index = python.index("n")
print(index)
index = python.index("n", index+1)
print(index)

print(python.find("Java")) # 값이 포함되지 않을 경우: -1
#print(python.index("Java")) # 오류 
#print("hi")
print(python.count("n")) # n이 몇번 나왔는지 개수

# 문자열 포맷
# 방법 1
print("나는 %d살입니다."%20)
print("나는 %s을 좋아해요"%"파이썬")
print("Apple 은 %c로 시작해요"%"A")
# %S
print("나는 %s색과 %s색을 좋아해요" %("파란","빨간"))

# 방법2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))

# 방법3
print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간", age=20))

# 방법4
age = 20
color="빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")

# 탈출문자 \n:줄바꿈
print("백문이 불여일견 \n백견이 불여일타")
# \" \' : 문장내에서 따옴표
print('저는 "나도코딩"입니다.')
print('저는 \"나도코딩\"입니다.')

# \\ : 문장내에서 \
print("C:\\Users\\hyj\\Desktop\\PythonWorkspace")

# \r: 커서를 맨앞으로 이동
print("Red Apple\rPine")

# \b: 백스페이스(한글자 삭제)
print("Redd\bApple")

# \t탭
print("Red\tApple")


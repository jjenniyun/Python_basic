# 표준 입출력
# print("Python", "Java", "JavaScript", sep=" vs ")
print("Python", "Java", sep=",", end="?")
print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# 시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
    # print(subject, score)
    # print(subject.ljust(8), str(score).rjust(4), sep=":") # 왼쪽 뒤에 8개 정렬이 되게 하고 오른쪽4개 정렬되도록 함
    
# 은행 대기순번표
# for num in range(1,21):
    # print("대기 번호 : "+str(num).zfill(3))

answer = input("아무 값이나 입력하세요 : ") # 항상 문자열 형태로 저장
print("입력하신 값은 "+answer+"입니다.")

# 다양한 출력 포맷
# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 때 +로 표시, 음수일 때 -로 표시
print("{0: >+10}".format(500))
print("{0: >-10}".format(-500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(500))
# 3자리마다 콤마를 찍어주기
print("{0:,}".format(10000000))
# 3자리마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(10000000))
print("{0:+,}".format(-10000000))
# 3자리마다 콤마를 찍어주기, 부호도 붙이고 자릿수 확보하기
# 돈이 많으면 행복하니까 빈자리는 ^로 채워주기
print("{0:^<+30,}".format(1000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수까지만 표시
print("{0:.2f}".format(5/3))
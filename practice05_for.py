# rnadrange()
for waiting_no in range(1,6): 
    print("대기 번호 : {0}".format(waiting_no))
    
star = ["아이언맨","토르","아이 엠 그루트"]
for customer in star:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    
absent = [2,5] # 결석
no_book = [7] # 책을 깜빡함
for student in range(1,11): # 1~10
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))
    
# 출석번호가 1,2,3,4 앞에 100을 붙이기로 함 →101,102, 103, 104
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor","I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor","I am groot"]
students = [i.upper() for i in students]
print(students)
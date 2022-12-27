# 매주 1회 작성해야 하는 보고 서가 있는 아래와 같은 형태로 출력하라
# - X 주차 주간보고 -
# 부서:
# 이름:
# 업무 요약:

# 1~50주차까지의 보고서 파일을 만드는 프로그램 작성하기
# 조건 : 파일명은 '1주차.txt', '2주차.txt' ... 와 같이 만들기

for i in range(1,51):
    with open(str(i)+"주차.txt","w", encoding="utf-8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :") # 파일이 많아 삭제함!
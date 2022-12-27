# 사이트별로 비밀번호를 만들어 주는 프로그램 작성

# 예) http://naver.com
# 규칙1) http:// 부분 제외 → naver.com
# 규칙2) 처음 만나는 점(.) 이후 부분은 제외 → naver
# 규칙3) 남은 글자 중 처음 세자리 +글자 갯수+글자내'e'갯수 +"!" rntjd
# 예) 생성된 비밀번호 : nav51!

url = "http://youtube.com"
my_str = url.replace("http://","") # 규칙1
#print(my_str)
my_str = my_str[:my_str.index(".")] # 규칙2
#print(my_str)
password = my_str[:3]+str(len(my_str))+ str(my_str.count("e"))+"!" # 규칙3
print("{0}의 비밀번호는 {1}입니다.".format(url,password))
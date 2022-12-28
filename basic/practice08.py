# score_file = open("score.txt", "w", encoding="utf-8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf-8")
# score_file.write("과학: 80")
# score_file.write("\n코딩: 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.read())
# score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
#print(score_file.readline()) # 줄별로 읽기, 한줄 익고 커서는 다음줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# while True:
    # line = score_file.readline()
    # if not line:
        # break
    # print(line, end="")
# score_file.close()

lines = score_file.readlines() # list형태로 저장
for line in lines:
    print(line, end="")
    
score_file.close()

# pickle
import pickle
# profile_file = open("profile.pickle","wb")
# profile = {"이름":"조규성", "나이":25, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

with open("profile.pickle","rb") as profile_file:
    print(pickle.load(profile_file)) # close할 필요 없음
    
with open("study.txt", "w", encoding="utf-8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")
    
with open("study.txt","r",encoding="utf-8") as study_file:
    print(study_file.read())
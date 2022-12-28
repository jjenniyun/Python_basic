# 딕셔너리 {}
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) # 오류 : 5라는 키가 없기 때문에
# print(cabinet.get(5)) # none
# print(cabinet.get(5,"사용가능")) 
# print("hi")

print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3":"유재석","B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"]= "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 둘만 출력
print(cabinet.keys())

# value둘만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)
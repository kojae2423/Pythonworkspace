## 사전 ##

cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet[5]) cf. []를 쓸땐, 오류가 나면, 다음문장 출력은 불가!
print(cabinet.get(5)) # cf. .get을 쓰면 오류가 나도, None하고, 다음문장 출력은 가능.
print(cabinet.get(5, "사용 가능")) # 5가 None이면, 뒤에 것을 출력한다.
print("hi")

print(3 in cabinet) # True, 3이 저 변수 안에 있냐?
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["c-20"] = "조세호" # cabinet에 c-20이라는 값을 만들고, 그 값은 조세호다.
                           # 만약, c-20이 존재한다면, 업데이트 된 값.
print(cabinet)

# 간 손님

del cabinet["A-3"] # "A-3"은 삭제!
print(cabinet)

# key 들만 출력
print(cabinet.keys()) # dict_keys(['B-100', 'c-20']) 이 키들이 남아있다.

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet) # 모든값 삭제.



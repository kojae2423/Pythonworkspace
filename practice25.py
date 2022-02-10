## 표준 입출력 ##

# print("Python", "Java", sep=",", end="?") # end는 ?를 넣어버림으로써 한 문장으로 표현이 된다.
# print("무엇이 더 재밌을까요?")

# 출력 
# Python,Java?무엇이 더 재밌을까요?

# import sys
# print("Python", "Java", file=sys.stdout) 
# print("Python", "Java", file=sys.stderr) 

# 시험 성적
scores = {"수학":0, "영어":50,"코딩":100}
for subject, score in scores.items(): # key,value 같이 뽑기 위해 items 사용!
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust(8) : 8칸의 공간을 남기고 왼쪽으로 정렬, rjust(4) : 4칸의 공간을 남기고 오른쪽으로 정렬

# print(subject, score) 일때,
#출력
# 수학 0
# 영어 50
# 코딩 100

# 은행 대기순번표
# 001, 002, 003, ....
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # zfill(3)은 3개만큼의 공간을 확보하는데, 값이 없는 공간은 0으로 채운다는 뜻.

answer = input("아무 값이나 입력하세요 : ") # 값을 입력하면 그값이 문자형태로 answer에 들어가서 밑에 코드가 실행된다.
print("입력하신 값은 " + answer + "입니다.") # 숫자를 넣었는데 string값으로 나오는 이유는 input을 쓰게 되면 항상 문자열 형태로 받는다!!
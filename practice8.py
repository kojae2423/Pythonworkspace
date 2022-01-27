## 문자열 처리함수 ##

python = "Python is Amazing"
print(python.lower()) # 소문자로 출력
print(python.upper()) # 대문자로 출력
print(python[0].isupper()) # 첫번째 글자가 대문자니?
print(len(python)) # 글자수
print(python.replace("Python", "Java")) # 내가 설정한 문자를 다른 문자로 대체한다.


index = python.index("n") # n이 몇번째에 있냐?
print(index)
index = python. index("n", index + 1) # n을 찾은 인덱스 1번 다음부터 n을 찾아줘.
print(index)

print(python.find("Java")) # find로 찾을때, 값이 없으면 -1로 나온다.
# print(python.index("Java"))  index로 찾을때, 값이 없으면 에러! 그 다음 프로그램은 실행이 안된다.
#  하지만, find는 무시하고 실행을 한다.
print("hi")

print(python.count("n")) # n이 몇개 있는지 찾아줘.


## 탈출 문자 ##

print("백문이 불여일견\n백견이 불여일타") # \n : 줄바꿈

# 저는 "고재형"입니다. = 이것을 출력하고싶다!(밑에 참고)
# print("저는 "나도코딩"입니다.") = 에러!
print("저는 '고재형'입니다.")
print('저는 "고재형"입니다.') # 큰따옴표로 표기 하고 싶을떄.

## 우리는 지금까지 ""를 사용했는데, 여기서''이거를 사용 하면 헷갈리기 때문에
## 쓸수 있는게 탈출문자이다!!

print("저는 \"고재형\"입니다.") # \", \'는 문장내에서 따옴표 사용가능!
print('저는 \'고재형\'입니다.') 

# \\ : 문장 내에서 \ 로 바뀐다.
print(" C:\\Users\\pc\\Desktop\\Pythonworkspace>") # 문장내에서 그냥 \ 하나인 것은 알수 없는 문자로 처리되서, \\를 써서 \ 처럼 보이게 해야한다. 

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple 출력. \r뒤에문장을 앞으로 끌어다 쓰는거?!?

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple") # RedApple 출력.

# \t : 탭
print("Red\tApple") # Red   Apple 출력.

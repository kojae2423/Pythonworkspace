## 기본값 ##

# def profile(name, age, main_lang) :
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
#         .format(name, age, main_lang)) # \를 치면, 밑에 하나의 문장이다.

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업. => 나이, 언어는 같을거다. 그래서 똑같이 계속 적어줄 필요가 없어서 기본값을 설정한다.!!

def profile(name, age=17, main_lang="파이썬") : # 호출 받았을때, age, main_lang가 설정 되지 않으면 그대로 기본값으로 호출된다는 뜻.
     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
         .format(name, age, main_lang))

profile("유재석")
profile("김태호")

## 키워드값 ##

def profile(name, age, main_lang) :
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")  # 순서가 뒤바껴도 키워드를 적어주면 그대로 출력이 된다.
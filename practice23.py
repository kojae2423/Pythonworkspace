## 가변인자 ##

# def profile(name, age, lang1, lang2, lang3, lang4, lang5) :
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end는 문장이 출력되고 나서, 다음줄에 다음 코드가 출력되는게 아니라 다음 칸에 그대로 출력된다.
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language) : # *로 시작되는 매개변수를 이용
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end는 문장이 출력되고 나서, 다음줄에 다음 코드가 출력되는게 아니라 다음 칸에 그대로 출력된다.
    for lang in language:
         print(lang, end=" ")
    print() # 이 부분은 잘 이해가 안되긴 하지만, 줄바꿈을 위해서 사용했다?

profile("유재석", 20, "python", "Java", "C", "C++", "C#", "Javascript")
profile("김태호", 25, "Kotlin", "Swift",)

# 유재석의 lang을 추가하고 싶은데, 그러려면 함수 자체를 바꿔야 한다. 이것을 안하려고 사용하는게 "가변인자"다!!

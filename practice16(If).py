## IF ##
# weather = "맑아요"
# weather = input("오늘 날씨는 어떄요? ") # 이 문장이 출력되고, 거기에 조건을 입력하면, 밑에 코드가 실행된다.
# # if 조건 : 
# #     실행 명령문

# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요") #if 조건이 충족 안되면, 그 다음 조건문!!
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else :
#     print("준비물 필요 없어요.")

temp = int(input("기온은 어떄요? ")) # 기온은 정수기 때문에, int로 묶어준다.
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp <30:
    print("괜찬은 날씨에요")
elif 0 <= temp < 10 :
    print("외투를 챙기세요")
else: # 그 외 나머지
    print("너무 추워요. 나가지 마세요")
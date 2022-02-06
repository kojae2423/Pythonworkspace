## while ## 어떤 조건이 만족할 때까지 반복한다.
# customer = "토르"
# index = 5  # 5번을 확인하기 위해
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# 출력 : 토르, 커피가 준비 되었습니다. 5 번 남았어요.
    # 토르, 커피가 준비 되었습니다. 4 번 남았어요.
    # 토르, 커피가 준비 되었습니다. 3 번 남았어요.
    # 토르, 커피가 준비 되었습니다. 2 번 남았어요.
    # 토르, 커피가 준비 되었습니다. 1 번 남았어요.
    # 커피는 폐기처분되었습니다.

# customer = "아이언맨"
# index = 1
# while True : ## while True 는 계속!
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer,index))
#     index += 1

# 종업원에게 찾아오는 사람이 토르면 음료를 준다.

customer = "토르"
person = "Unknown"

while person != customer :  # person이 내가 원하는 customer가 올때까지 반복한다.
         print("{0}, 커피가 준비 되었습니다.".format(customer))
         person = input("이름이 어떻게 되세요? ")

## 내가 부른 손님이면, 반복문 탈출!
    
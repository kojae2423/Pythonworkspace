## 지역변수 & 전역변수 ##

# 지역변수 : 함수내에서만 사용 가능.함수가 호출될때 만들어졌다가, 호출이 끝나면 사라진다.
# 전역변수 : 프로그램 모든 내에서 쓸수있다. / 일반적으로 많이 쓰면 코드 관리가 어려워진다. 가급적 x

gun = 10

def checkpoint(soldiers) : # 경계근무 / checkpoint라는 함수를 만들고, soldiers라고 전달값을 받겠다.
    gun = 20 # 지역변수
    gun = gun - soldiers # gun은 checkpoint 안에서 만들어진 gun(지역변수) / gun = 20이 없다면 에러가 난다.
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun)) # 밖에 있는 gun을 받는다.
checkpoint(2) # 2명이 경계 근무 나감 / checkpoint라는 함수를 호출했기 때문에, def안에 있는 gun이 사용된다.
print("남은 총 : {0}".format(gun)) # 호출 후에는 또 밖에 있는 gun이 작동된다.

##출력##

# 전체 총 : 10
# [함수 내] 남은 총 : 18
# 남은 총 : 10

def checkpoint(soldiers) : # 경계근무 
    global gun # 전역 공간에 있는 gun 사용 / 전역변수
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun)) 
checkpoint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))

##출력##

# 전체 총 : 10
# [함수 내] 남은 총 : 8
# 남은 총 : 8

## 전달값 & 반환값으로 써버리자.

def checkpoint_ret(gun, soldiers) :
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun # 바뀌어진 변수 gun 값을 밖으로 던져 줄수 있다.

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2) # retuen한 변수 값을 받는다.
print("남은 총 : {0}".format(gun))

##출력##

# 전체 총 : 10
# [함수 내] 남은 총 : 8
# 남은 총 : 8

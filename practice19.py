## continue & break

absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡함
for student in range(1, 11) : # 1,2,3,4,5,6,7,8,9,10
    if student in absent : 
        continue  # 아래 있는 문장을 실행시키지 않고, 다음 반복(for)으로 실행을 하라.
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break # 뒤에 반복문이 있던 없던, 바로 실행을 끝낸다.
    print("{0}, 책을 읽어봐".format(student))
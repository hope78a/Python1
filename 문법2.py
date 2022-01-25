print("숫자 함수  --------------------")
from math import *
print(floor(4.99))  # 내림 4
print(ceil(3.14))   # 올림 


print("랜덤 함수  --------------------")
from random import *
print(random())         #0.0 ~ 1.0
print(random() * 10)    # 0 ~ 10.0
print(int(random() * 10))    # 0 ~ 10
print(int(random() * 10) + 1)    # 1 ~ 10

# 로또 번호 6개
print(int(random() * 45) + 1)    # 1 ~ 45
print(int(random() * 45) + 1)    # 1 ~ 45
print(int(random() * 45) + 1)    # 1 ~ 45
print(int(random() * 45) + 1)    # 1 ~ 45
print(int(random() * 45) + 1)    # 1 ~ 45
print(int(random() * 45) + 1)    # 1 ~ 45

print(randrange(1, 46))  #1~45 숫자
print(randint(1, 45))    #1~45 숫자

date = randrange(4,28)    #연습문제
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")


# https://www.youtube.com/watch?v=kWiCuklohdY
# 강의 47분까지 청취
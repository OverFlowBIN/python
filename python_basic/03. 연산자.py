print((2 + 3) * 4)
print(2 + 3 * 4)
number = (2 + 3) * 4
print(number)
number += 4
print(number)
number *= 2
print(number)
number /= 2
print(number)
number %= 5
print(number)
number -= 2
print(number)
number //= 2
print(number)


print(abs(-5))
print(pow(4, 2))
print(max(3,67,3,13,324))
print(min(3,67,3,13,324))
print(round(3.14)) # 반올림
print(round(3.49999999999999999999999)) # 반올림 ???????
print(round(3.49)) # 반올림

# from math import * # math library 모든걸 다 쓰겟다
import math
print(math.floor(4.623123123))
print(math.ceil(4.1))
print(math.sqrt(16))

from math import * # math library 모든걸 다 쓰겟다
print(floor(4.623123123))
print(ceil(4.1))
print(sqrt(16))

# 랜덤 함수
from random import *
print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)  # 1.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))
print(int(random() * 10))
print(int(random() * 10))

print(int(random() * 10) + 1) # 1~10 이하 랜덤 정수
print(int(random() * 10) + 1)
print(int(random() * 10) + 1)
print(int(random() * 10) + 1)
print(int(random() * 10) + 1)
print(int(random() * 10) + 1)


# 로또 값 출력
print(int(random() * 45) + 1) # 1~45 이하 랜덤 출력
print(int(random() * 45) + 1) # 1~45 이하 랜덤 출력
print(int(random() * 45) + 1) # 1~45 이하 랜덤 출력
print(int(random() * 45) + 1) # 1~45 이하 랜덤 출력
print(int(random() * 45) + 1) # 1~45 이하 랜덤 출력

print(randrange(1,46)) # 1~46 미만 랜덤 출력

print(randint(1,45)) # 1~45 이하 랜덤 출력


# Quiz
from random import *
date = int(random() * 24) + 4
print("오프라인 스터티 모임 날짜는 매월" + str(date) + "일로 선정되었습니다.")

date = randrange(4,29)
print("오프라인 스터티 모임 날짜는 매월", date, "일로 선정되었습니다.")

date = randint(4,28)
print(f"오프라인 스터티 모임 날짜는 매월 {date}일로 선정되었습니다.")

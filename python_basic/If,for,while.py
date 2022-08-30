import imp
from random import randrange


print('========================== IF =============================')
print('')
# 조거문 if

# weater = input("오늘 날씨는 어때요?")
# if weater =='비' or "눈":
#   print("우산을 챙기세요")
# elif weater == '미세먼지':
#   print("마스크를 챙기세요")
# else:
#   print('준비물 필요 없어요.')

# temp = int(input('온도가 몇도인가요?'))
temp = 20
if 30 <= temp:
  print('너무 더운 나가지마셈')
elif 10 <= temp and temp < 30:
  print('날씨 좋네 나가세요')
elif 0 <= temp < 10:
  print("외투 챙겨서 나가셈")
else:
  print("너무 추움 나가지마..")
  
  
  
print('')  
print('========================== FOR =============================')
print('')

# print('대기번호 : 1')
# print('대기번호 : 2')
# print('대기번호 : 3')
# print('대기번호 : 4')

for waiting_no in range(1, 6):
  print("대기번호 : {}".format(waiting_no))  
  # 또는 print("대기번호 : %s"%(waiting_no))
  
  
starbucks = ['아이언맨', '토르', '아이엠그루트']
for customer in starbucks:
  print("{}님, 커피가 준비 되었습니다.".format(customer))
  
  
  
print('')  
print('========================== WHILE =============================')
print('')

customer = "토르"
index = 5
while index >= 1:
  print("{}님, 커피 준비되었습니다. {}번 남았습니다.".format(customer, index))
  index -= 1
  if index == 0:
    print('커피는 버릴게~')
    
customer = "아이언맨"
index = 0
while True: # 무한 루프
  print("{}님, 커피 준비되었습니다. {}번 호출입니다.".format(customer, index))
  index += 1
  if index == 1:
    break
  

customer = "토르"
person = "Unkown"
while person != customer:
  print("{}님, 커피가 준비 되었습니다. 넌 누구니?".format(customer))
  # person = input('넌 이름이 뭐니? ' ) or "토르"
  person = "토르"
  
  
  
print('')  
print('========================== CONTINUE, BREAK =============================')
print('')


absent = [2, 5]
no_book = [7]
for student in range(1, 11):
  if student in absent:
    continue
  elif student in no_book:
    print("책을 안가져와? 오늘 수업 끝 {}번 너는 교무실로 와라".format(student))
    break
  print("{}번 학생, 책 읽어라!".format(student))
  
  
  
  

print('')  
print('========================== FOR (ONE LINE) =============================')
print('')


# 출석번호 1 2 3 4, 앞에 100을 붙이기로 => 101, 102, 103, 104 (like JS map())
students = [1,2,3,4]
print(students)

students = [i + 100 for i in students]
print(students)


# 학생이름을 길이로 변환
students = ['Iron man', 'Thor', 'Im groot']
print(students)

students = [i.upper() for i in students]
print(students)

students = [i.lower() for i in students]
print(students)

students = [len(i) for i in students]
print(students)




print('')  
print('========================== FOR (ONE LINE) =============================')
print('')


# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님이다.
# 50명의 승객과 매칭 기회가 있을 떄, 총 탑승 승객 수를 구하는 프로그램을 작성하라.

# 조건1: 승객별 운행 소요 시간은 5~ 50분 사이의 난수로 정해진다.
# 조건2: 당신은 소요시간 5~15분 사이의 승객만 매칭해야 한다,.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탕습 승객 : 2명

from random import *

customers = []
idx = 0
while idx < 50:
  customers.append(randrange(5, 51))
  idx += 1

print(customers)  

count = 0;
index = 1
for time in customers:
  if(5 <= time <= 15):
    print ("[O] {}번째 손님 (소요시간 : {}분)".format(index, time))
    count += 1
  else:
    print ("[ ] {}번째 손님 (소요시간 : {}분)".format(index, time))
  index += 1

print('')
print('총 탑승 승객 : {}'.format(count))


# print(customer)
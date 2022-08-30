# 리스트

# 지하철 칸별로 10명, 20명, 30명
from os import remove
from random import shuffle


subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway[1])

# 사람1은 몇번째 index?
subway = ['사람1', '사람2', '사람3' ]
print(subway.index('사람1'))

# 사람3 추가하기
subway.append('사람4')
print(subway)

# 중간에 추가하기 insert(index, element)
subway.insert(1, '추가사람')
subway.insert(1, '추가사람')
print(subway)

# 뒤에서 꺼내기 pop()
print(subway.pop())
print(subway)

# 동일한 element 확인하기
print(subway.count('추가사람'))

# 정렬
num_list = [5,4,11,3,2,1,0]
num_list.sort()
print(num_list)

# 뒤집기
num_list.reverse()
print(num_list)

# 리스트 모든 내용 삭제하기
num_list.clear()
print(num_list)
num_list = [5,4,11,3,2,1,0]

# 다양한 형태의 값
mix_list = ['사람1', 20, True]
print(mix_list)

# 리스트 합치기
mix_list.extend(num_list)
print(mix_list)

print('')
print('========================== dictionary =============================')
print('')

# dictionary (key, value)
cabinet = {3: '사람3', 100: '사람100'}
print(cabinet[3])
print(cabinet[100])

# dictionary get
# print(cabinet[5])  => 오류가 되어 프로그램이 멈춘다..
print(cabinet.get(3))
print(cabinet.get(5)) # None으로 출력
print(cabinet.get(5, "사용가능 KEY")) # 5라는 Key가 사용 안하고 있다면 "사용가능 KEY"로 출력된다.

print(3 in cabinet) # True
print(5 in cabinet) # False

# dictionary key -> string으로 사용
cabinet = {'3': '사람3', '100': '사람100'}
print(cabinet.get('3'))
print(cabinet.get('100'))

# dictionary add
print(cabinet)
cabinet['20'] = '사람20'
print(cabinet)

# dictionary update
print(cabinet)
cabinet['20'] = '사람200'
print(cabinet)

# dictionary delete
print(cabinet)
del cabinet['20']
print(cabinet)

# key, value 만 출력
print(cabinet.keys())
print(cabinet.values())

# key, value 모두 출력
print(cabinet.items())

# dictionary clear
cabinet.clear()
print(cabinet)


print('')
print('========================== Tuple =============================')
print('')

# Tuple
# list와 다르게 내용변경 및 추가를 할 수 없지만 속도가 list보다 빠르다.

menu = ('돈까스', '치즈까스')
print(menu)
print(menu[0])
print(menu[1])

# Tuple add
# => 오류가 난다. 고정된 값만 사용 가능하다.

# Tuple Usage
# name = '김종국'
# age = 20
# hobby = 'coding'

(name, age, hobby) = '김영빈', 20, '코딩'
print(name)
print(name, age, hobby)


print('')
print('========================== Set =============================')
print('')

# 집합(Set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,4,4,5}
print(my_set)

java = {'사람1', '사람2', '사람3' }
python = {'사람1', '사람4', '사람5' }

# 교집합(java, python 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합 (java ok, python no)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남 add
print(python)
python.add('사람3')
print(python)

# java에서 삭제 remove
print(java)
java.remove('사람1')
print(java)



print('')
print('========================== 자료구조간 변경 =============================')
print('')


menu2 = {'커피', '우유','주스'}
print(menu2, type(menu2))

menu2 = list(menu2)
print(menu2, type(menu2))

menu2 = tuple(menu2)
print(menu2, type(menu2))

menu2 = set(menu2)
print(menu2, type(menu2))




print('')
print('========================== Quiz =============================')
print('')

# 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 줄가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# (활용 예제)
# form random import *
# 1st = [1,2,3,4,5]
# print(1st)
# shuffle(1st)
# print(1st)
# print(sample(1st, 1))

from random import *
# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
users = range(1, 21) # type이 range이다

print(users)
lst = list(users)

print(lst)
shuffle(lst)

winners = sample(lst,4)

print(f"-- 당첨자 발표 ---\n치킨당첨자 : {winners[0]}\n커피당첨자 : {winners[1:]}\n-- 축하합니다 --")


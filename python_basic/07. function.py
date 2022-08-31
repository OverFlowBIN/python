# function
from codecs import getencoder


print('========================== FUNCTION =============================')
print('')

def open_account():
  print("새로운 계좌가 생성되었습니다.")
  
def deposit(balance, money): # 입금
  print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
  return balance + money

def withdraw(balance, money): # 출금
  if balance >= money:
    print('출금이 완료되었습니다. 잔액은 {0}원 입니다.'.format(balance - money))
    return balance - money
  else:
    print('출금이 완료되지 않았습니다 잔액은 {0}원 입니다.'.format(balance))
    return balance
  
def withdraw_night(balance, money):
  commission = 100
  return commission, balance - money - commission # 여러게 값을 콤마(,)를 통해 Tuple 형식으로 리턴함

balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원 이며, 잔액은 {1}원 입니다.".format(commission, balance))




print('')
print('========================== DEFAULT VALUE IN FUNCTION =============================')
print('')


def profile(name, age=20, main_lang="python"): # age에 defalut를 줬다면 뒤에 있는 argument도 defalut 값을 줘야 한다.
  print("이름: {0}, 나이 : {1}, 주 사용 언어 : {2}".format(name, age, main_lang))

profile('overflowbin') # 해당 값이 없으면 defalut값으로 사용된다
profile('bin11788')



print('')
print('========================== KEYWORD IN FUNCTION =============================')
print('')


def profile2(name, age, main_lang):
  print(name, age, main_lang)
  
profile2(name="유재석", main_lang="python", age=21)
profile2(main_lang="js",name="김태호",  age=32)



print('')
print('========================== 가변인자 =============================')
print('')

def profile3(name, age, lang1, lang2, lang3, lang4, lang5):
  print("이름: {0}, 나이 : {1}".format(name, age), end = ', ')
  print('lang :', lang1, lang2, lang3, lang4, lang5)
  
# profile3("유재석", 20, 'python', 'java', 'js', 'c', 'c++')
# profile3("김태호", 32, 'Kotlin', 'swift', '', '', '')
# 이런식으로 argument의 갯수가 변해야 하는 상황일때 가변인자를 사용한다.

def profile4(name, age, *languages):
  print("이름: {0}, 나이 : {1}".format(name, age), end = ', lang :')
  for lang in languages:
    print(lang, end = ' ')
  print()
    
profile4("유재석", 20, 'python', 'java', 'js', 'c', 'c++', 'c#', 'go')
profile4("김태호", 32, 'Kotlin', 'swift')



print('')
print('========================== 지역변수, 전역변수 =============================')
print('')


gun  = 10

def checkpoint(soldiers):
  # global gun # 전역 공간에 있는 gun 사용
  gun = gun - soldiers
  print("[함수 내] 남은 총 : {}개".format(gun))
  
  
def checkpoint_return(gun, soldiers):
  gun = gun - soldiers
  print("[함수 내] 남은 총 : {}개".format(gun))
  return gun
  
print("전체 총 : {}개".format(gun))
# checkpoint(2)
gun = checkpoint_return(gun, 2)
print("남은 총 : {}개".format(gun))


print('')
print('========================== Function QUIZ =============================')
print('')

# Quiz) 표준 체중을 구하는 프로그램을 작성하시오
#  * 표준 체중 : 각 개인의 키에 적당한 체중
 
#  (성별에 따른 공식)
#   남자 : 키(m) x 키(m) x 22
#   여자 : 키(m) x 키(m) x 21
  
# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : height, gender
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
  
  if gender == 'male':
    weight = round(height * height * 22, 2)
    height = round(height * 100)
    print('키 {}cm 남자의 표준 체중은 {}kg 입니다.'.format(height, weight))
  else:
    weight = round(height * height * 21, 2)
    height = round(height * 100)
    print('키 {}cm 여자의 표준 체중은 {}kg 입니다.'.format(height, weight))
    
std_weight(1.75, 'male')
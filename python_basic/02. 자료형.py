# int
print(5)
print(-10)
print(3.14)
print(5+3)
print(2*8)
print(3*(3+1))


# string
print('풍선')
print("나비")
print("나비"*10)


# boolean
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not 5 < 10)


# practice
animal = "강아지"
name = '구슬'
age = 4
hobby = "산책"
is_adult = age >= 3

print(f"우리집 {animal} 이름은 {name}이에요")
print(f"{name}는 {age}살이며 취미는 {hobby}입니다.")
print(name + "는 " + str(age) + "살이며 취미는 " + hobby + "입니다.")
print(name,"는 ", age, "살이며 취미는 ", hobby, "입니다.")


# Quiz 변수를 이용하여 다음 문장을 출력해라
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")

station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")

station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")


# 연산자
print(1+1)
print(3-1)
print(5*2)
print(6/3)

print(2**3)
print(5%3)
print(10%3)
print(5//3) # 몫 1
print(10//3) # 몫 3

print(10 > 3)
print(4 >= 7)
print(10 < 3)
print(5 <= 5)

print(5 == 5)
print(3 == 5)
print(10 == 5*2)

print(1 != 3)
print(not(1 != 3))

print(3 > 0 and 3 > 5)
print(3 > 0 & 3 < 5)
print(3 > 0 or 3 > 5)
print((3 > 0) | (3 > 5))

print(5 > 4 > 3)
print(5 > 4 > 6)  # and 연산자로 생각하기.

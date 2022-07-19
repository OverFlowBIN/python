# 문자열
sentence = "나는 소년입니다."
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = '''파이선은 쉬워요 1
파이선은 쉬워요 2
파이선은 쉬워요 3'''
print(sentence3)

sentence3 = '''
파이선은 쉬워요 1
파이선은 쉬워요 2
파이선은 쉬워요 3
'''
print(sentence3)


# 슬라이싱
jumin  = "990102-1178456"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0~2 직전까지
print("월 : " + jumin[2:4]) 
print("일 : " + jumin[4:6]) 

print("생년월일 : " + jumin[0:6])
print("생년월일 : " + jumin[:6])

print("뒤 7자리 : " + jumin[7:14])
print("뒤 7자리 : " + jumin[7:])

print("뒤 7자리(뒤에서부터) : " + jumin[-7:]) # 맨뒤에서 7번쨰부터 끝까지


# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("python", "Java")) # 찾을 문자열의 대소문자를 정확히 찾아줘야 한다.
print(python.replace("Python", "Java")) 

index = python.index("n")  # 만약 여기서 원하는 값이 없으면 오류가 나서 프로그램이 종료된다.
print(index)
index = python.index("n", index + 1) # 두번째 인자는 해당 위치(포함) 부터 찾으라는 뜻
print(index)

print(python.find("n"))
print(python.find("Java"))  # 포함되지 않을떄는 -1

print(python.count("n"))  # 해당 인자가 몇번 포함되어있는지 출력


# 문자열 포맷
print("a" + "b")
print("a",   "b")

print("나는 %d살입니다." % 20)  # d는 정수만
print("나는 %s을 좋아한다." % "파이선")  # s는 string만
print("Apple은 %c로 시작한다." % "A")  # c는 스펠링만

print("나는 %s과 %s를 좋아한다." % ("파이선", "자바"))

print("나는 {}살입니다.".format(20))
print("나는 {}살이고 {}입니다.".format(20, "남자"))
print("나는 {0}살이고 {1}입니다.".format(20, "남자")) # 나는 20살이고 남자입니다.
print("나는 {1}살이고 {0}입니다.".format(20, "남자")) # 나는 남자살이고 20입니다.

print("나는 {age}살이고 {gender}입니다.".format(age = 20, gender = "남자")) # 나는 남자살이고 20입니다.

age = 20
gender = "여자"
print(f"나는 {age}살이고 {gender}입니다.")


# 탈출문자 (\n : 줄바꿈)
print("백문이 불여일견 \n백견이 불여일타")

print("저는 \"아무개\" 입니다")
print('저는 \'아무개\' 입니다')


# \\ 역슬러쉬 2개
print("C:\\User\\nadocoding\\desktop")


# \r : 커서를 맨 앞으로 이동
print("Red Appe\rPine")


# \b : 백스페이스 (한글자 삭제)
print("Redd\bApple")


# \b : tap
print("Red\tApple")



#quiz
url = "http://naver.com"
url = "http://google.com"
res = url.replace("http://", "")
index_dot = res.index('.')
res = res[:index_dot]
length = len(res)
num_e = res.count("e")
password = res[:3] + str(length) + str(num_e) + "!"

print("{}의 비밀번호는 {}입니다.".format(url, password))
print("{1}의 비밀번호는 {0}입니다.".format(password, url))
print("%s의 비밀번호는 %s입니다."%(url, password))





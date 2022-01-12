# 빈 list 만들기

score_list = [] 
print(score_list)
score1 = 50
score_list.append(score1)
print(score_list)
person_list = list()
print(person_list)
person1 = "Sumi"
person_list.append(person1)
print(person_list)

# range(10) = 0~ 9 
# list(range()) -> range를 list로 바꿔줌 
a = list(range(10))
print(a)

# range 증가폭 사용 
# range 끝나는 숫자는 생성되는 숫자에 포함되지 않음
b = list(range(10,2,-1))
print(b)

c = list(range(-3,9,2))
print(c)
c = tuple(c)
print(c)


# 요소가 한 개 들어있는 튜플 
element1 =(38)
print(element1, type(element1))

element2 = (38,)
print(element2, type(element2))

menu = ["한식", "양식", "중식", "일식"]
print(menu)
menu = tuple(menu)
print(menu)
menu = list(menu)
print(menu)

# 문자열을 list와 tuple안에 넣으면, 문자 하나하나가 리스트, 튜플의 요소로 들어감
From = list("Hello")
print(From)
To = tuple("Hello")
print(To)

# 입력 값을 변수 2개에 저장하기
x = input().split() # 리스트 형태로 반환
print(x)
a, b, c = x # str 형태로 입력 값이 변수에 저장 
print(a,b,c, type(a), type(b), type(c)) 
a = int(a) # 정수형으로 변환시켜주기  
a += 1 
print(a)


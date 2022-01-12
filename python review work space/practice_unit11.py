from random import *

number = []
# random으로 중복되지 않는 다섯개의 숫자 뽑기
while len(number) < 5 :
    a = randint(1,10)
    if a not in number: 
        number.append(a)
        # 4개까지 추가시킨 후, number의 length가 5가 되지 않았으므로
        # while문 한번 더 돌리고, 5개까지 추가시킨 후 while문 종료
print(number)
number.sort()
print(number)

b = int(input()) 
# input = str형이므로 정수형으로 변환해 사용해야
#  number list에 이 숫자가 있는 지 확인 가능
print(b in number)

p = "Hello, My dear"
print("v" in p) # 문자열은 따옴표 잊지 말기!

l_list = list(range(10)) + list(range(11,18))
print(l_list)

print("Hello, My dear-" + str(90)) 
# 정수형을 + 로 문자열과 연결할 때는 str() 붙여주기!
print("Hello, My dear" , str(90), sep = "-")

print(list(range(-4,10,2)))
# range에 len 함수를 사용하면 숫자가 생성되는 개수를 구함
print(len(range(-4,10,2)))

# sequence 객체에서 [] 대괄호를 사용하면 
# 실제로는 __getitem__메서드를 호출하여 요소를 가져옴
# 시퀸스객체.__getitem__(index)
str_index = p.__getitem__(2) 
print(str_index)
str_index = p.__getitem__(3)
print(str_index)

str1 = "Python is amazing"
print(str1.upper()) # 괄호 잊지말기
print(str1.lower())
print(str1[:6]) # 끝나는 숫자는 포함안됨
print(str1[-1]) # 마지막 요소
print(len(str1))
print(str1[5:18])
print(str1[len(str1)-1]) # 마지막 요소
print(str1[3:6])
print(str1[2:13:3])
print(str1[:])
print(str1[::-1])
print(str1[0:len(str1)])

# slice 객체 이용해서 슬라이싱 
s = slice(0,6,2)
print(str1[s])
print(str1.__getitem__(s))

num_list = [0,10,20,30,40]
num_list[:3] = ["a","b","c"]
print(num_list)
# del num_list[:-2]
del num_list[0::2]
print(num_list)

# range는 *를 이용하여 반복 불가


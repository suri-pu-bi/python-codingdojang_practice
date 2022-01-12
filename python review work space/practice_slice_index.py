year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]

print(year[-3:])
print(population[5:])

n= [-32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2]
print(n[1::2])
print(n[1:len(n):2])

# 심사문제
x = input().split()
# print(x)
# x = tuple(x) tuple는 del를 사용할 수 없음. 추가/변경 불가
del x[-5:]
# x = tuple(x)
print(tuple(x))

str1 = input()
str2 = input()
print(str1[1::2]+str2[0::2])
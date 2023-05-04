# 페이지 네비게이션하기
#총건수, 페이지당 보여줄수, 총페이지수
#5,10,1
#15,10,2
#25,10,3
#30,10,3

def getTotalPage(m,n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1  #무조건 1페이지 필요하니 하나빼야됨 1,2,3,4 출력됨

print(getTotalPage(5,10))
print(getTotalPage(15,10))
print(getTotalPage(25,10))
print(getTotalPage(30,10))

a = 1.5
print(type(a))

b = [1,2,2,2,3,3]
d = [2,2,5,6]
newList = list(set(b))
print(newList)


#집합
b = set([1,2,2,2,3,3])
d = set([2,2,5,6])
print(b & d)

a = True
print(type(a))


a = [1,2,3]
b = a
a[1] = 4

print(id(a))
print(id(b))








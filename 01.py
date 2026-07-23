#메모리 주소 반환하는 함수 id()

a =10
print(id(10))


a= 20
print(id(a))

b = type(a)
print(b)

c = 10.5
d = a + c # 암시적 형변환
print(d)

f = 'hello'

print(f[::-1])

word = 'hello'
print(word[::-1])

age = 29
height = 158.78
name = '장다정'

# 변수를 print 로 출력하는 방식
# 파이써닉 하지 않다.
print('제이름은', name, '이고, 나이는', age)

# 변수를 출력하는 가장 pythonic 한 방식은 뭘까?
# f-string
print(f'제 이름은 {name}이고, 나이는 {age}, 키는 {height:.1f}')
# {height:.1f} -> 소수 1자리까지 반올림

my_tuple = (1,)
my_tuple2 = (1)
print(my_tuple)
print(my_tuple2)
print(type(my_tuple))
print(type(my_tuple2))

# print(int("3.14"))
print(float("3"))

a, b = 1, 2
# a, b = (1, 2) => tuple 게념이 적용 돼서 가능한 것
print (a, b)

print(list(range(1, 10)))
print(list(range(10, 1, -1))) # 10부터 1 전까지 -1씩 해서 출력 그니까 2~10 출력되는거
#----------------------------------------------------------------------------------------
arr = [3, 4, 5]
print(id(arr))
# 위 아래 id 값 같음
arr[2] = 7
print(id(arr))

arr= [6, 7, 8]      # 얘는 id 값 달라짐
print(id(arr))
#-----------------------------------------------------------------------------------------
a = {}              # 딕셔너리 초기화
my_set = set()      # 세트 초기화
my_dict = dict()    # 딕셔너리 초기화

print(type(a))
print(type(my_set))
print(type(my_dict))

#-----------------------------------------------------------------------------------
x = ''
y = None

print(type(x))
print(type(y))


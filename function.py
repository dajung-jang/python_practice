def make_sum(pram1, pram2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """
    result = pram1 + pram2
    return result

# 함수 호출
result = make_sum(100, 30)
print(result)

value = print("hello world")
print(value)


# global 키워드 사용 이유
# 전역변수 수정하기 위해

a = 30
def kfc():
    global a 
    a = 10
    b = 20
    print(a);



temps = [0, 20, 30, 37, 100]

result = list(map(lambda x: x * 9/5 + 32, temps))

#def dgree(x):
#    return x*9/5 +32

#result = list(map(dgree, temps))

print(*result)

temps = [0, 20, 30, 37, 100]
result = map(lambda x: x * 9/5 + 32, temps)
print(*result)
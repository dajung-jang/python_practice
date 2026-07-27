# =============================================================
# [심화] 매직 메서드 (Magic Method / Dunder Method)
# - 앞뒤로 언더바 2개가 붙은 메서드 (__init__, __str__ 등)
# - 던더(dunder) = Double UNDERscore
# - 특징: 우리가 직접 부르지 않아도 '특정 상황에서 자동으로' 호출됨
#   __init__  => 인스턴스를 만들 때 자동 호출
#   __str__   => print()로 인스턴스를 출력할 때 자동 호출
# =============================================================

class Circle:
    def __init__(self, radius):
        self.radius = radius

    # __str__ 메서드 정의
    # 인스턴스를 문자열로 표현할 때 호출됨
    # print(c1) 호출 시 사용됨
    # 이 메서드를 정의하면 인스턴스를 print()로 출력할 때 더 읽기 쉬운 형식으로 출력됨
    # __str__ 메서드는 문자열을 반환해야 함
    def __str__(self):
        return f'원의 반지름: {self.radius}'


# =============================================================
# __str__을 정의하지 않았다면 print(c1)은
# <__main__.Circle object at 0x...> 같은 알아보기 힘든 형태로 출력됨
# - __str__을 정의해두면 print()가 이 메서드의 반환값을 대신 보여줌
#   => 객체를 사람이 읽기 좋은 형태로 표현할 수 있음
# =============================================================

c1 = Circle(10)
c2 = Circle(1)

print(c1)  # 원의 반지름: 10
print(c2)  # 원의 반지름: 1

# --------------------------------------------
# 강사님 추가 설명
# @ : 데코레이터
# 매직 메서드, 클래스 메서드, 스태틱 메서드

class calculator:
    pi = 3.141592   # 클래스 변수

    # 생성자 메서드 
    def __init__(self, name):
        self.name = name    # 인스턴스 변수

    # 메서드
    def add(self, a, b):
        return a + b

    # 매직 메서드 ---> 객체를 문자열로 표현할 때 호출 됨
    def __str__(self):
        return f'calculator name : {self.name}'

    # 클래스 메서드 ---> 클래스 자체를 첫 번째 인자로 받는다.
    @classmethod
    def get_pi(cls):
        return f'파이(pi)의 값은 {cls.pi}다.'

    # 스태틱 메서드 ---> 인자로 self 나 cls 가 X / 독립적으로 실행 가능
    @staticmethod
    def multiply(a, b):
        return a * b

# 인스턴스 생성
calc = calculator('카시오 공학용 계산기')    # 그냥 ()로 끝내지 않는 이유: 초기 생성할때 name 을 받는다고 해놨기 떄문에
# 메서드 호출
print(calc.add(5, 7))
# 매직 메서드 호출 : 인스턴스 할당한 변수
print(calc)     # 만약 위에서 __str__ 을 return 이 아닌 print 로 작성했다면 print(calc) 이 아닌 그냥 calc 만 쳐도 같은 결과값 나옴
# 클래스 메서드 호출 : 클래스로 직접 호출
print(calculator.get_pi())
# 스태틱 메서드 호출
print(calculator.multiply(100, 100))   # 클래스로 직접 호출
print(calc.multiply(100, 100))        #

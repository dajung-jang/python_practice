# =============================================================
# 예외 처리 (Exception Handling) - try / except
# - 예외(Exception): 실행 중에 발생하는 에러 (문법 오류와 다름)
# - 예외가 발생하면 프로그램이 그 자리에서 '비정상 종료'됨
# - try-except는 에러가 나도 멈추지 않고 대응하도록 해줌
#   try   : 에러가 날 수 있는 코드를 넣는 곳
#   except: 특정 예외가 발생했을 때 대신 실행할 코드
# =============================================================

# =============================================================
# try 블록에서 10 / 0 => ZeroDivisionError 발생
# - 예외가 나는 순간 try의 나머지는 건너뛰고 except로 점프
# - 프로그램이 죽는 대신 안내 메시지를 출력하고 정상 진행
# - except 뒤에 예외 이름을 적으면 '그 예외일 때만' 잡음
# =============================================================

# try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')

# =============================================================
# 아래는 주석 처리된 예시 (필요 시 해제하여 실습)
# - int()는 숫자로 바꿀 수 없는 문자열을 받으면 ValueError 발생
#   예) 'abc' 입력 시 => except ValueError로 처리됨
# =============================================================

try:
    num = int(input('숫자입력 : '))
except ValueError:
    print('숫자가 아닙니다.')

# --------------------------------

# 추가 메모

# 내장 예외(Built-in Exceptions)
#  : 예외 상황을 나타내는 예외 클래스들
# - 파이썬에서 이미 정의되어 있으며, 특정 예외 상황에 대한 처리를 위해 사용
# - 이런 예외를 사용하면 오류에 맞는 적절한 처리 방법 적용 가능

# 1. ZeroDivisionError 
#   : 나누기 또는 모듈로 연산의 두번째 인자가 0일 때 발생
# 10/0    # ZeroDivisionError: division by zero

# 2. TypeError : 타입 불일치
# '2' + 2     # TypeError: can only concatenate str (mot "int") to str

# 3. NameError : 지역 또는 전역 이름 찾을 수 없을 때 발생
# print(name1)    # NameError: name 'name1' is not defined

# 4. TypeError : 인자 누락
# sum()       # TypeError: sum() takes at least 1 posotional argument (0 given)

# 5. TypeError : 인자 초과


try:
    x = int(input('숫자를 입력하세요:'))
    y = 10 / x
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('유요한 숫자가 아닙니다.')
else:
    print(f'결과: {y}')
finally:
    print('프로그램이 종료되었습니다.')
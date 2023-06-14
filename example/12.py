# 오류와 예외 처리
# 풀이 시간 : 5분

result = 0
try:
    [1, 2, 3][3]
    "a" + 1
    4 / 0

except TypeError:
    result += 1

except ZeroDivisionError:
    result += 2

except IndexError:
    result += 3

finally:
    result += 4

# 결과는 7이 나올 것이다. 그 이유는 try문의 첫번째 줄에서 IndexError로 예외가 발생하면서 try문을 빠져나오고 except문에 의해 3이 더해진다.
# 그리고 finally문으로 넘어가서 4가 더해지므로 result = 7이 출력될 것이다.

# try - except - else문 : 예외가 발생하지 않을 경우 else문이 실행됨
# try - except - finally문 : 예외 발생 여부에 상관없이 마지막에 finally문이 실행됨

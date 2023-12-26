### 가변 인자 ###

# 파이썬에서 함수를 정의할 때 인자값의 개수를 가변적으로 정의해야 하는 경우도 있음
# 이 경우 *args와 같이 함수 파라미터 앞에 *를 붙여주면 됨


# Positional variable argument (*args)
def foo(*args):
    print(args)


# 위 코드를 실행하면 다음과 같이 두 개의 튜플이 출력됨
# 함수 호출시 args라는 변수는 여러 개의 입력에 대해 튜플로 저장한 후 이 튜플 객체를 바인딩함
foo(1, 2, 3)
foo(1, 2, 3, 4)


# Keyword variable arguments (**kwargs)
def foo(**kwargs):
    print(kwargs)


foo(a=1, b=2, c=3)


# *args와 **kwargs 같이 사용하기
def foo(*args, **kwargs):
    print(args)
    print(kwargs)


foo(1, 2, 3, a=1, b=1, c=2)

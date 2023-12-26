### 익명 함수 활용 ###

# map 함수 기본 구조
# map(function, iterable)
# map() 함수는 반복 가능한 객체의 각 요소에 대해 function 함수를 적용한 결과를 새로운 iterator로 반환함

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_a = list(map(lambda x: str(x) if x % 3 == 0 else x, a))
print(f"{new_a=}")


# filter는 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져오는데
# 첫번째 파라미터인 함수의 반환값이 True일 때만 해당 요소를 가져옵니다.
b = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
new_b = list(filter(lambda x: x > 5 and x < 10, b))
print(f"{new_b=}")

list()

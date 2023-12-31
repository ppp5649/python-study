# 리스트 더하기와 extend 함수
# 풀이 시간 : 5분

a = [1, 2, 3]
print(a)
print(id(a))


# a 객체 원본의 요소에 4와 5를 추가 (객체가 변하지 않기 때문에 주소 값 그대로)
print(a.extend([4, 5]))
print(a)
print(id(a))

# a라는 새로운 객체에 a + [4, 5]가 할당됨 (새로운 객체이기 때문에 주소 값 바뀜)
a = a + [4, 5]
print(a)
print(id(a))

# 결괏값에는 차이가 없지만 [1,2,3,4,5]라는 list가 새로운 객체에 할당되냐 안되냐의 차이

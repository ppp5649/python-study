# 리스트 총합 구하기
# 풀이 시간 : 2분

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

# 새로운 리스트를 만들어 내장함수 sum()을 이용한 방법
# 객체를 새로 할당 해야하기 때문에 메모리 낭비

# new_A = [num for num in A if num >= 50]
# answer = sum(new_A)

# 새로운 리스트를 만들지 않기 때문에 A의 길이가 길 경우 메모리 성능 향상
answer = 0

for num in A:
    if num >= 50:
        answer += num

print(answer)

# filter 함수 첫번째 파라미터 함수로 들어감

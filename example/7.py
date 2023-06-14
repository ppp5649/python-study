# 한 줄 구구단
# 풀이 시간 : 6분

n = int(input())

# join()은 str으로 이루어진 iterable 객체를 합쳐서 str으로 반환하는 함수이기 때문에 n * i를 str으로 형 변환이 필요하다.
mul = [str(n * i) for i in range(1, 10)]
answer = " ".join(mul)

print(answer)

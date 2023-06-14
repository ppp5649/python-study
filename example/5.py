# 피보나치 함수
# 풀이 시간 : 10분


# %%
def fibo(n):
    answer = [0, 1]

    while True:
        answer.append(answer[-1] + answer[-2])
        # n보다 큰 요소가 포함될 경우 마지막 요소 제거하고 break
        if answer[-1] > n:
            answer.pop()
            break

    return answer


print(fibo(13))

# %%

# Duplicate Numbers
# 풀이 시간 : 10분

from collections import Counter

nums = input().split(" ")
booleans = []


for num in nums:
    cnt_num = Counter(num)
    # value값 기준으로 내림차순 정렬
    cnt_num = sorted(cnt_num.items(), key=lambda x: x[1], reverse=True)
    # value값이 가장 큰 tuple이 cnt_num의 첫번째 요소이기 때문에 cnt_num[0][1]이 1보다 큰 지 확인하면 됨
    print(cnt_num)
    if cnt_num[0][1] > 1:
        booleans.append("false")
    else:
        booleans.append("true")

answer = " ".join(booleans)
print(answer)

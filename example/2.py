# 딕셔너리 값 추출하기
# 풀이 시간 : 5분

a = {"A": 90, "B": 80}

if "C" not in a:
    a["C"] = 70

a.update({"C": 70})

# dic.get(key, defalut value)
# get() 함수는 key값이 존재하지 않을 때 defalut 값을 대신 가져온다.

print(a.get("C", 70))  # C라는 key가 존재하지 않기 때문에 70을 가져온다.
print(a)  # a의 원본은 여전히 A와 B밖에 존재하지 않은다.

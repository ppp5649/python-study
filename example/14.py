# 문자열 압축하기
# 풀이 시간 : 40분


def press_str(s):
    stack = [s[0]]
    idx_check = []
    answer = ""

    # stack의 마지막 요소와 다른 문자가 등장했을 때 문자와 stack의 길이를 더해주고 stack을 비움
    for i in range(1, len(s)):
        if stack[-1] != s[i]:
            answer += f"{stack[-1]}{len(stack)}"
            stack.clear()
            idx_check.append(i)

        stack.append(s[i])

    # 마지막으로 바뀌는 문자 처리
    if answer[-2] != s[-1]:
        answer += f"{s[-1]}{len(s)-idx_check[-1]}"

    return answer


def press_str(s):
    stack = [s[0]]
    idx_check = [0]
    answer = ""

    # stack의 마지막 요소와 다른 문자가 등장했을 때 문자와 stack의 길이를 더해주고 stack을 비움
    for i in range(1, len(s)):
        if stack[-1] != s[i]:
            idx_check.append(i)

        stack.append(s[i])

    idx_check.append(len(s))

    for i in range(len(idx_check) - 1):
        answer += f"{s[idx_check[i]]}{(idx_check[i + 1] - idx_check[i])}"

    return answer


# 좀 더 컴팩트하게 짤 수 있을 것 같은데 마지막으로 바뀌는 문자 처리 부분이 약한 것 같다. 비슷한 유형도 공부해봐야 할듯
print(press_str("aabbcccccc"))

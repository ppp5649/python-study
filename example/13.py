# DashInsert 함수
# 풀이 시간 : 15분


def dash_insert(s):
    stack = [s[0]]

    for i in range(1, len(s)):
        # 짝수 연속
        if int(stack[-1]) % 2 == 0 and int(s[i]) % 2 == 0:
            stack.append("*")
        # 홀수 연속
        elif int(stack[-1]) % 2 != 0 and int(s[i]) % 2 != 0:
            stack.append("-")

        stack.append(s[i])

    answer = "".join(stack)
    return answer


print(dash_insert("4534333"))

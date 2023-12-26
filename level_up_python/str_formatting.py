### 문자열 포맷팅 ###
# 가장 먼저 살펴볼 코드는 C언어 스타일의 문자열 포맷팅입니다.
# C언어를 배운 사람들에게는 익숙한 방법인데 %s는 문자열을 %d는 정수형을 의미합니다.

name = "HJ"
score = 90

# C언어 스타일
print("%s's score is %d." % (name, score))

# format 메서드
print("{}'s scroe is {}".format(name, score))

# f-string
print(f"{name}'s scroe is {score}.")

### 특수한 글자 출력 ###
data = 3
print("{{ {} }}".format(data))
print(f"{{ {data} }}")

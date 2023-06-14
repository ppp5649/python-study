# 역순 저장
# 풀이 시간 :
file_path = "txt/abc.txt"
new_file_path = "txt/reverse_abc.txt"

# with문을 사용해서 파일을 open하면 with문을 빠져나가는 순간 자동으로 close된다.
with open(file_path, "r") as f:
    lines = f.readlines()
    lines = lines[::-1]

# strip : 개행문자 제거
with open(new_file_path, "w") as f:
    for line in lines:
        line = line.strip()
        f.write(line)
        if line != lines[-1]:
            f.write("\n")

# lines = f.readlines()
# lines = lines[::-1]

# for line in lines:
#     line = line.strip()
#     f.write(line)

# f.close()

# readable한지 아닌지 체크하는 것도 중요한 듯

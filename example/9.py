# 평균값 구하기
# 풀이 시간 : 10분

file_path = "txt/sample.txt"
new_file_path = "txt/result.txt"

total = 0

with open(file_path, "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        total += int(line)

with open(new_file_path, "w") as f:
    f.write(str(total / len(lines)))

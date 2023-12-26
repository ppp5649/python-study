# import subprocess

# # output = subprocess.check_output("tasklist")
# # data = output.decode("cp949")
# # lines = data.splitlines()

# # for line in lines:
# #     print(line)

# cmd = "ps -ef"
# # subprocess.run(cmd, shell=True)

# result = subprocess.run(cmd, capture_output=True, shell=True, encoding="utf-8")
# print(result.stdout)

import subprocess

cmd = "pstree"
process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
while True:
    output = process.stdout.readline()
    if output == "" and process.poll() is not None:
        break
    if output:
        print(output.strip())

# Longest Common Prefix


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # 가장 짧은 문자열을 앞에 두기 위해 길이로 sort (sort 함수의 parameter로 정렬의 기준이 되는 함수를 넣을 수 있음)
        strs.sort(key=len)

        answer = ""
        prefix_arr = []

        for i in range(len(strs[0])):
            for j in range(len(strs)):
                # strs 각 요소들의 prefix를 prefix_arr에 넣어줌
                prefix_arr.append(strs[j][i])

            # set 함수를 이용해 중복 제거한 후 개수가 1개라면 모든 prefix가 동일하다는 의미이므로 answer을 갱신해줌
            if len(set(prefix_arr)) == 1:
                answer += prefix_arr[0]

            # if문을 만족하지 않으면 prefix가 될 수 없으므로 반복문을 끝냄
            else:
                break

            prefix_arr = []

        return answer


solution = Solution()

print(solution.longestCommonPrefix(["flower", "flow", "flight"]))


### sorted 함수의 key parameter를 이용한 딕셔너리 정렬 ###

dic = {"B": 35, "A": 12, "C": 40, "D": 5}

# key 기준 오름차순 정렬
sorted_dic_val = sorted(dic.items(), key=lambda x: x[1])

# value 기준 오름차순 정렬
sorted_dic_key = sorted(dic.items(), key=lambda x: x[0])

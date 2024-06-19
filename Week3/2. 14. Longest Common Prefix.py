'''
https://leetcode.com/problems/longest-common-prefix/description/
'''

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(0, len(strs[0])):
            for string in strs:
                if i == len(string) or string[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res


def main():
    res = Solution().longestCommonPrefix(['flower', 'fl', 'flow'])
    print(f"Result is: {res}")

main()
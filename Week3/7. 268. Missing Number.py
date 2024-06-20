'''
https://leetcode.com/problems/missing-number/description/
'''

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        expected = 0
        for i in range(0, len(nums)+1):
            expected += i
        return expected - total

def main():
    number = Solution().missingNumber([4, 5, 6, 7, 2, 0, 3])
    print(number==1)

main()
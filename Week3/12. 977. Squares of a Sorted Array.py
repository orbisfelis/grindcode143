'''
https://leetcode.com/problems/squares-of-a-sorted-array/description/
'''

from typing import List
from collections import deque

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = deque()
        l, r = 0, len(nums)-1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                answer.appendleft(left * left)
                l += 1
            else:
                answer.appendleft(right * right)
                r -= 1
        return list(answer)

def main():
    res = Solution().sortedSquares([-2, 0, 2, 4, 100])
    print(f'{res == [0,4,4,16,10000]}')

main()
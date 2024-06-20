'''
    https://leetcode.com/problems/move-zeroes/description/
'''
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        
        return nums

def main():
    test = [0, 1, 3, 0, 12]
    test = Solution().moveZeroes(test)
    if test == [1, 3, 12, 0, 0]:
        print('PASS')
    else:
        print('FAIL')

main()
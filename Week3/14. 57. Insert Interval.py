'''
https://leetcode.com/problems/insert-interval/description/
'''

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        left, right = 0, len(intervals)-1
        target = newInterval[0]

        while left <= right:
            mid = left + (right - left)//2
            if intervals[mid][0] < target:
                left = mid+1
            else:
                right = mid-1
        
        intervals.insert(left, newInterval)

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0] :
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

def main():
    res = Solution().insert([[1,3],[6,9]], [2,5])
    print(res == [[1,5], [6,9]])

main()
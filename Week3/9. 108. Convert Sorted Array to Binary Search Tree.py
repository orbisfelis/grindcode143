'''
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
'''

from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            root = None
            if left <= right:
                mid = left + (right - left)//2
                root = TreeNode(nums[mid])
                root.left = helper(left, mid-1)
                root.right = helper(mid+1, right)
            return root

        return helper(0, len(nums)-1)

def main():
    res = Solution().sortedArrayToBST([-10,-3,0,5,9])

    expected_nums = [0,-10,5,None,-3,None,9]
    res_nums = []

    def bfs(root):
        queue = deque()

        if root:
            queue.append(root)

        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.popleft()
                res_nums.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
    
    bfs(res)
    print(res_nums)
    print(expected_nums)
    print(f'{expected_nums == res_nums}')

main()

'''
    https://leetcode.com/problems/palindrome-linked-list/description/
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
class Solution:
    '''
        O(n) time but O(n) space.
    '''
    def isPalindromeSlower(self, head: Optional[ListNode]) -> bool:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        
        l, r = 0, len(stack) - 1
        while l <= r:
            if stack[l] != stack[r]:
                return False
            l += 1
            r -= 1
        return True

    '''
    O(n) and O(1) space complexity
    '''
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        l, r = head, prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True
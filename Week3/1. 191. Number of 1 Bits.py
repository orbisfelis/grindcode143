'''
    Write a function that takes the binary representation of a positive integer and returns the number of set bits
 it has (also known as the Hamming weight).
    https://leetcode.com/problems/number-of-1-bits/
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n = n & (n-1)
            res += 1
        return res


def main():
    res = Solution().hammingWeight(11)
    print(f'Result is: {res}')

main()
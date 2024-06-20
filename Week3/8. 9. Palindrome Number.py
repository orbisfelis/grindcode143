'''

'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        temp = x
        reverse = []
        while temp > 0:
            digit = temp % 10
            reverse.append(digit)
            temp = temp // 10
        
        original = reverse[::-1]
        return original == reverse
    

def main():
    res = Solution().isPalindrome(121)
    print(res == True)

    res = Solution().isPalindrome(-121)
    print(res == False)

main()
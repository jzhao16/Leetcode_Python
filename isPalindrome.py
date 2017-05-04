class Solution(object):
    def isPalindrome(self, x):
        if x <=0 or (x!=0 and x % 10 == 0):
            return False
        else:
            rev = 0
            while x > rev:
                rev = rev*10 + x%10
                x = x /10
            if x == rev or x == rev/10:
                return True
            else:
                return False
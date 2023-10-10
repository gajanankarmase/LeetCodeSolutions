class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        os = ""
        for i in s:
            if i.isnumeric() or i.isalpha():
                os += i
        
        if os == os[::-1]:
            return True
        else:
            return False

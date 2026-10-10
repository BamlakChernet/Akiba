class Solution:
    def isPalindrome(self, x: int) -> bool:
     value=str(x)
     reverse=value[::-1]
     if  value==reverse:
       return  True
     else:
        return False
    

import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = re.sub('[\W_]+', '', s)
        result = result.lower()
        
        if result == result[::-1]:
            return True
        return False
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_itr = 0
        
        if len(s) == 0:
            return True

        for letter in t:
            if s[s_itr] == letter:
                s_itr += 1
            if s_itr == len(s):
                return True
        
        return False
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_sorted = sorted(s)
        t_sorted = sorted(t)

        if len(s) == len(t):
            if s_sorted == t_sorted:
                return True
            else:
                return False
        else:
            return False
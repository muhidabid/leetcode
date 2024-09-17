class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        tokens = s.split()
        return " ".join(tokens[::-1])
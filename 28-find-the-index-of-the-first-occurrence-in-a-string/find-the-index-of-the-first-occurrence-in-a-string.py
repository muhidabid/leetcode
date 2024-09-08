class Solution(object):
    def helper(self, start, haystack, needle):
        needle_iterator = 0
        haystack_iterator = start
        
        while haystack_iterator < len(haystack):
            print("n:", needle_iterator, "h:", haystack_iterator)
            if needle[needle_iterator] == haystack[haystack_iterator]:
                needle_iterator += 1
                haystack_iterator += 1
                if needle_iterator == len(needle):
                    return start
            else:
                break
        return -1

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index = 0

        while index < len(haystack):
            if haystack[index] == needle[0]:
                helper_result = self.helper(index, haystack, needle)
                if helper_result != -1:
                    return helper_result
            index += 1
        
        return -1
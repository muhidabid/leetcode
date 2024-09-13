class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        sorted_citations = sorted(citations)
        for i, citation in enumerate(reversed(sorted_citations)):
            if i+1 >= citation:
                if citation != 0:
                    if citation < i:
                        return i
                    else:
                        return citation
                else:
                    return i
            elif i+1 == len(sorted_citations):
                return i+1
        return 0
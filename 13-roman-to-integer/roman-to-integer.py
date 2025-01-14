class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        v = 0
        i = 0
        while i < len(s):
            print(v, i)
            if s[i] == 'I':
                if i+1 < len(s):
                    if s[i+1] == 'V':
                        v += 4
                        i = i + 2
                        continue
                    elif s[i+1] == 'X':
                        v += 9
                        i = i + 2
                        continue
                v += 1
            elif s[i] == 'V':
                v += 5
            elif s[i] == 'X':
                if i+1 < len(s):
                    if s[i+1] == 'L':
                        v += 40
                        i = i + 2
                        continue
                    elif s[i+1] == 'C':
                        v += 90
                        i = i + 2
                        continue
                v += 10
            elif s[i] == 'L':
                v += 50
            elif s[i] == 'C':
                if i+1 < len(s):
                    if s[i+1] == 'D':
                        v += 400
                        i = i + 2
                        continue
                    elif s[i+1] == 'M':
                        v += 900
                        i = i + 2
                        continue
                v += 100
            elif s[i] == 'D':
                v += 500
            elif s[i] == 'M':
                v += 1000
            i = i + 1
        return v
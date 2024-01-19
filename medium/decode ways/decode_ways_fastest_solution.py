class Solution:
    def numDecodings(self, s: str) -> int:
        f, g = 0, 1
        for i, c in enumerate(s, 1):
            if c != "0":
                h = g
            else:
                h = 0

            j = s[i - 2]
            if i > 1 and j != "0" and int(s[i - 2 : i]) <= 26:
                h += f

            f, g = g, h
        return g

s = Solution()
print(s.numDecodings("1127"))
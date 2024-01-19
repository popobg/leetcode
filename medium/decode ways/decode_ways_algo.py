
# encode = a message with letters convert into numbers ("A" = 1, ..., "Z" = 26)
# decode = a message with digits corresponding to letters
# There are multiple ways to decode a message : "1106" can be 1 1 10 6 = "AAJF", or 11 10 6 = "KJF".
# The grouping 1 11 06 is incorrect because F is 6 and not 06.
# Given a string s containing only digits, return the number of ways to decode it.
# The test cases are generated so that the answer fits in a 32-bit integer.

def fib(n: int) -> int:
    """return the number of fibonacci starting by 3"""
    if n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    fn1 = 1
    fn2 = 1
    for _ in range(3, n + 1):
        fn = fn1 + fn2
        fn1 = fn2
        fn2 = fn

    return fn2

def split(string: str) -> list[str]:
    """split the string into parts if a number outside [1, 2] is found"""
    # ex: "12131210121"
    split = []
    tmp = ""

    for c in string:
        tmp += c

        i = int(c)
        if i > 2 or i == 0:
            if tmp == "0":
                return None
            split.append(tmp)
            tmp = ""

    if len(tmp) > 0:
        split.append(tmp)
    # ex: ["1213", "1210", "121"]
    return split

class Solution:
    def numDecodings(self, string: str) -> int:
        """return the number of ways a string of digits can be decode with A --> 1,..., Z --> 26"""
        res = 0
        # ex: "12131210121"
        parts = split(string)
        # ["1213", "1210", "121"]

        # if parts == None
        if not parts:
            return 0

        for part in parts:
            # if part contains a 0, this part has fib(n - 1) ways to be decode
            if "0" in part:
                subres = fib(len(part) - 1)

            # if part has a combination > 26, this part has fib(n) ways to be decode
            elif len(part) > 1 and int(part[-2:]) > 26:
                subres = fib(len(part))

            # if part has no combination > 26 and no 0, it has fib(n + 1) ways to be decode
            else:
                subres = fib(len(part) + 1)

            if res == 0:
                res = subres

            else:
                res *= subres

        # the result (number of ways of the string) is the product of the ways of each subpart
        return res

s = Solution()
print(s.numDecodings("113027"))
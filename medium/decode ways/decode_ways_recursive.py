class Solution:
    def __init__(self):
        # the attribut which stocks the number of ways the string can be decode
        self.ways = 0

    # compter le nombre de chemins valides dans self.ways
    def explore_string(self, string):
        """the recursive function that parse the string and calculate the number of way"""
        # when the string has no char in it, we are at the end of a way
        if len(string) == 0:
            self.ways += 1
            return

        # return if the first char is a 0
        # a 0 can not be the first char, it is always associate with the previous char (always 1 or 2 to be valid)
        if string[0] == "0":
            return

        current_string = ""
        # for loop which parse the string given in each recursion
        for char in string:
            current_string += char
            if int(current_string) <= 26:
                # call recursively the function for a shorter string
                self.explore_string(string[len(current_string):])
            else:
                # return if the current string > 26
                return

    def numDecodings(self, s: str) -> int:
        """overall function that calculate the number of ways a string can be decode"""
        self.ways = 0
        self.explore_string(s)
        return self.ways


s = "01127"
sol = Solution()
print(sol.numDecodings(s))

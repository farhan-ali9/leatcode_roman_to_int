class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        total=0
        pre_val=0
        for char in reversed(s):
            curr_val = dict[char]
            if curr_val >= pre_val:
                total+=curr_val
            else:
                total-=curr_val
            pre_val = curr_val
        return total

# leatcode_roman_to_int

# Roman to Integer Conversion

The given code defines a class Solution with a method romanToInt that converts a Roman numeral string to an integer.

# Method Signature

def romanToInt(self, s):
self: The instance of the class (implicit parameter).



s: The input Roman numeral string.

# Approach


The conversion from Roman numerals to integers follows a specific set of rules. The code uses a dictionary to map each Roman numeral character to its corresponding integer value.


Initialize a variable total to keep track of the total value.


Initialize a variable pre_val to store the previous value during iteration.



Iterate over the characters of the input string s in reversed order.


For each character, get its integer value from the dictionary.



If the current value is greater than or equal to the previous value, add it to the total.



Otherwise, subtract it from the total.



Update the pre_val with the current value for the next iteration.




Return the final total value.



# Example

solution = Solution()


result = solution.romanToInt("IX")


print(result)


# Output:


9

The Roman numeral "IX" represents the number 9 in decimal notation.

# Complexity Analysis


The time complexity of this approach is O(n), where n is the length of the input string s. 

This is because we iterate over each character of the string once.

The space complexity is O(1) since the dictionary and variables used have constant space requirements.

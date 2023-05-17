"""
Question 2: -
Consider a string to be valid if all characters of the string appear the same number of times.
It is also valid if he can remove just one character at the index in the string,
and the remaining characters will occur the same number of times.
Given a string, determine if it is valid. If so, return YES , otherwise return NO
"""

def check_valid(string):
    str_dict = dict()
    for char in string:
        if not str_dict.get(char,False):
            str_dict[char] = 1
        else:
            str_dict[char] += 1

    values = list(str_dict.values())
    unique_val = set(values)

    if len(unique_val) == 1:
        return 'Yes'
    if len(unique_val) == 2:
        min_value = min(unique_val)
        max_value = max(unique_val)
        if values.count(min_value) == 1 and min_value == 1:
            return "YES"
        if values.count(min_value) == 1 and max_value - min_value == 1:
            return "YES"
    return 'No'


# Test case 1
test1 = "aabbcc"
test1_output = check_valid(test1)
print(f"Test case 1 valid: {test1_output}")

# Test case 2
test2 = "bbhhkkk"
test2_output = check_valid(test2)
print(f"Test case 2 valid: {test2_output}")




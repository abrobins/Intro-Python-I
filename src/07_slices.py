"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
new_list = a[1]
print(new_list)

# Output the second-to-last element: 9
neg_list = a[-2]
print(neg_list)

# Output the last three elements in the array: [7, 9, 6]
last3_list = a[-3:]
print(last3_list)

# Output the two middle elements in the array: [1, 7]
mid_list = a[2:-2]
print(mid_list)

# Output every element except the first one: [4, 1, 7, 9, 6]
skip_first = a[1:]
print(skip_first)

# Output every element except the last one: [2, 4, 1, 7, 9]
skip_last = a[:-1]
print(skip_last)

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
s_short = s[7:12]
print(s_short)

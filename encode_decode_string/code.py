# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Please implement encode and decode

# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
#                                 01234567
# One possible encode method is: "4#lint4#code4#love4#you"
#                                 i s
#                                  j

"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""
def encode(strs):
    res = ""
    for string in strs:
        res += str(len(string)) + "#" + string
    print(res)
    return res

"""
@param: str: A string
@return: dcodes a single string to a list of strings
"""
def decode(string):
    res, i = [], 0
    while i < len(string):
        j = i
        while string[j] != "#":
            j += 1
        length = int(string[i:j])
        res.append(string[j + 1 : j + length + 1])
        i = j + length + 1
    return res


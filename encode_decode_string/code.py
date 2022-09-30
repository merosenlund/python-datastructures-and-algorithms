"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""
def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

"""
@param: str: A string
@return: dcodes a single string to a list of strings
"""
def decode(str):
    res, i = [], 0
    while i < len(str):
        j = i
        while str[j] != "#":
            j += 1
        count = int(str[i:j])
        res.append(str[j + 1 : j + count + 1])
        i = j + count + 1

    return res

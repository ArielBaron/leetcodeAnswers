def longestCommonPrefix(strs):
    longestCommonPrefix = ""
    for index, char in enumerate(strs[0]):
        for i in range(len(strs)):
            if index + 1 > len(strs[i]) or strs[i][index] != char:
                return longestCommonPrefix
        longestCommonPrefix += char
    return longestCommonPrefix
#

print(longestCommonPrefix(["ab", "a"]))
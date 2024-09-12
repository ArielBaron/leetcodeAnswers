def Main():
    def Longest_Substring_Without_Repeating_Characters(s):
        longest_sub_string = 1
        seen_lst = []
        last_index = 0
        for index in range(len(s)):
            for char in s[last_index:len(s)]:
                if char not in seen_lst:
                    seen_lst.append(char)
                else:
                    break
            last_index += len(seen_lst)
            if len(seen_lst) > longest_sub_string:
                longest_sub_string = len(seen_lst)
            if longest_sub_string > len(s[last_index:len(s)]):
                print(longest_sub_string)
                return longest_sub_string
            seen_lst = []

        print(longest_sub_string)
        return longest_sub_string
    return Longest_Substring_Without_Repeating_Characters("pwwkew")

Main()

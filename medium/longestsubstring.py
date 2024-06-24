class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ''
        counter = ''
        for l in s:
            if l not in counter:
                counter += l

            else:
                if len(counter) > len(longest):
                    longest = counter
                counter = counter[counter.find(l)+1:] + l

        if len(counter) > len(longest):
            longest = counter
        return  len(longest)

string = "abcaatupac"

s = Solution()
longest = s.lengthOfLongestSubstring(string)
print(longest)
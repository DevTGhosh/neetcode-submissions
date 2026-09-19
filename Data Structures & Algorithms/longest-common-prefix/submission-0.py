class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result =""
        first_word=strs[0]
        arrayWord = []
        prevValue = ''
        for value in first_word:
            prevValue += value
            arrayWord.append(prevValue)

        for value in arrayWord:
            for v in strs:
                if not v.startswith(value):
                    return result
            result = value
        return result


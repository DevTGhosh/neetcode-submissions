class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # so letterArrayIndexes[0] = number of a's letterArrayIndexes[1] = no. of b's and so on
        stringHashMap = defaultdict(list)
        for i in strs:
            letterArrayIndexes = [0]* 26
            if len(i) == 0:
                stringHashMap['empty'].append("")
                continue
            for j in i:
                letterArrayIndexes[ord(j) - ord('a')] += 1
            stringHashMap[tuple(letterArrayIndexes)].append(i)

        return list(stringHashMap.values())
        

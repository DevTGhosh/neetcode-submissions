class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        #n = len(t) - 1
        #list_s = list(s)
        #list_t = list(t)
        dict_s = {}
        dict_t ={}
        #for i, value in enumerate(list_s):
        for value in s:
            if value in dict_s:
                a = dict_s[value]
                dict_s[value]= a + 1
            else:
                dict_s.setdefault(value, 1)
        
        for value in t:
            if value in dict_t:
                a = dict_t[value]
                dict_t[value]= a + 1
            else:
                dict_t.setdefault(value, 1)

        return dict_s == dict_t

        
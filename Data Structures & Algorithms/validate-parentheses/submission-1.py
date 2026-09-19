class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        correspondingHash = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for i in s:
            lastValue = stack[-1] if stack else None
            if i == '(' or i =='{' or i == '[':
                stack.append(i)
            elif lastValue != correspondingHash.get(i):
                stack.append(i)
                break
            else: 
                stack.pop()
        return len(stack) == 0    

        
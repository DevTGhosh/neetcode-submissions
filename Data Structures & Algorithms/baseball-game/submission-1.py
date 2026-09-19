class Solution:
    def calPoints(self, operations: List[str]) -> int:
        def is_int(s):
            try:
                int(s)
                return True
            except ValueError:
                return False
        pointsArray = []
        for i in operations:
            ap = len(pointsArray)
            lastValue = 0
            secondLastValue = 0
            if ap > 0:
                lastValue =  pointsArray[ap - 1]
            if ap > 1:
                secondLastValue = pointsArray[ap - 2]
            if is_int(i):
                pointsArray.append(int(i))
            elif i == '+':
                pointsArray.append(lastValue + secondLastValue)
            elif  i == 'D': 
                pointsArray.append(lastValue * 2)
            elif i == 'C':
                pointsArray.pop()
        return sum(pointsArray)
    
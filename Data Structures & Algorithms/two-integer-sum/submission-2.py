class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for idx, num in enumerate(nums):
            dict_nums.setdefault(num, []).append(idx)
        result =[]
        for index, value in enumerate(nums):
            remainder = target - value
            if remainder in dict_nums and dict_nums[remainder] != [index]:
                result.append(index)
                if remainder != value:
                    result.append(dict_nums[remainder][0])
                else:
                    result.append(dict_nums[remainder][1])
                break
        return result
                
            
        
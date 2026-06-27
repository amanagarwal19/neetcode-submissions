class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i in range(len(nums)):
            req = target-nums[i]
            if req in index:
                return [index[req],i]
            index[nums[i]] = i
            print(index)

        return []
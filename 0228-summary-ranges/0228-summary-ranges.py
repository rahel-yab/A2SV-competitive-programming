class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return nums
        elif len(nums) == 1:
            return [str(nums[0])]
        else:
            start = nums[0]
            end = nums[0]
            res = []
            for i in range(1, len(nums)):
                if nums[i] - nums[i-1] == 1:
                    end = nums[i]
                else:
                    res.append(to_str(start, end))
                    start = end = nums[i]
            res.append(to_str(start, end))  # This line should be outside the loop
            return res

def to_str(start, end):
    if start == end:
        return str(start)
    else:
        return str(start) + "->" + str(end)

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        seen = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
                seen = 1  # came across a new value, reset seen to 1
            elif seen < 2 and nums[i] == nums[i - 1]:
                nums[k] = nums[i]
                k += 1
                seen += 1

        return k
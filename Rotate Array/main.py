class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # If 101, avoid having to rotate 101 and only do 1 rotation
        k = k % len(nums)

        # If -k, this is equal to k plus len(nums)
        if k < 0:
            k += len(nums)

        # Reverse the first part of array
        self.reverse(nums, 0, len(nums) - k - 1)
        # Reverse the second part of array
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        # Reverse entire array
        self.reverse(nums, 0, len(nums) - 1)

    def reverse(self, nums, i, j):
        left_index = i
        right_index = j

        while left_index < right_index:
            temp = nums[left_index]
            nums[left_index] = nums[right_index]
            nums[right_index] = temp

            left_index += 1
            right_index -= 1
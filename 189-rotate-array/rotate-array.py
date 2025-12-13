class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=0
        while(i<n-(k%n)):
            nums.append(nums[0])
            nums.pop(0)
            i+=1

        
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)/2 > k:
            while k > 0:
                tmp = nums.pop()
                nums.insert(0,tmp)
                k = k-1
        elif len(nums) < k:
            k = k % len(nums)
            print(k)
            while k > 0:
                tmp = nums.pop()
                nums.insert(0,tmp)
                k = k-1
        else:
            k = len(nums)-k
            while k > 0:
                tmp = nums.pop(0)
                nums.append(tmp)
                k = k-1
        return nums
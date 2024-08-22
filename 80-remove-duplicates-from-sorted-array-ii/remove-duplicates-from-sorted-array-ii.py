class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        old_num = 0
        num_count = 0
        index_temp = 0

        for num in list(nums):
            if old_num != num:
                old_num = num
                num_count = 1
            else:
                num_count += 1
            
            if num_count > 2:
                nums.remove(num)
        
        return len(nums)
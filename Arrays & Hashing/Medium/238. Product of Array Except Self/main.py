class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # # Option 1 - using O(n) space [UNACCEPTABLE]
        # prefix_product = [nums[0]]
        # for i in range(1, len(nums)):
        #     prefix_product.append(nums[i] * prefix_product[-1])

        # suffix_product = [1] * len(nums)
        # suffix_product[-1] = nums[-1]
        # for i in range(len(nums) - 2, -1, -1):
        #     # i + 1 represents the number before nums[i]
        #     # before here from the right because with the
        #     # suffix approach you are going from right to left
        #     suffix_product[i] = nums[i] * suffix_product[i + 1]
        
        # # Product
        # product = []
        # for i in range(len(nums)):
        #     # There is no i-1 when i == 0, this will jump to the
        #     # end of the prefix_product which you don't want
        #     prefix = 1 if i == 0 else prefix_product[i - 1]
        #     # There is no i+1 when i == len(nums) - 1, i.e. at the
        #     # end of the list. This will give you out of bounds error
        #     # which you don't want
        #     suffix = 1 if i == len(nums) - 1 else suffix_product[i + 1]
        #     product.append(prefix * suffix)
        # return product

        # Option 2 - O(1) space
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result
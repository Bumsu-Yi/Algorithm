class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index +=1

        return index
    

sol = Solution()

# Test case 1
nums1 = [3, 2, 2, 3]
val1 = 3
print("Test case 1:")
print("Original array:", nums1)
print("Value to remove:", val1)
print("New length:", sol.removeElement(nums1, val1))
print("Modified array:", nums1)

# Test case 2
nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
print("\nTest case 2:")
print("Original array:", nums2)
print("Value to remove:", val2)
print("New length:", sol.removeElement(nums2, val2))
print("Modified array:", nums2)
# Given a list of integers "nums" and an integer "target",
# return indices of the two numbers such that they add up to "target".

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.

def find_target_sum(nums: list[int], target: int) -> list[int]:
    for index, n in enumerate(nums):
        index_add = index + 1

        while index_add < len(nums):
            if (n + nums[index_add]) == target:
                return [index, index_add]
            else:
                index_add += 1

nums1 = [2,7,11,15]
target1 = 9

nums2 = [3,2,4]
target2 = 6

nums3 = [3,3]
target3 = 6

print(find_target_sum(nums1, target1))
print(find_target_sum(nums2, target2))
print(find_target_sum(nums3, target3))
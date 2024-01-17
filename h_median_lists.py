# Given two sorted arrays (lists) nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

def find_median(nums1: list[int], nums2: list[int]) -> float:
    """find the median of two lists of numbers"""
    # faster than set union, less lines
    merged_list = sorted(nums1 + nums2)

    if len(merged_list) % 2 == 1:
        return float(merged_list[len(merged_list)// 2])

    else:
        return ((merged_list[(len(merged_list) // 2) - 1] + merged_list[(len(merged_list) // 2)]) / 2)

nums1 = [1, 3]
nums2 = [2]

nums3 = [1, 2]
nums4 = [3, 4]

nums5 = [24.1, 24.7, 25.0, 26.1]
nums6 = [25.2, 25.6, 25.7, 27.8]

print(find_median(nums1, nums2))
print(find_median(nums3, nums4))
print(find_median(nums5, nums6))
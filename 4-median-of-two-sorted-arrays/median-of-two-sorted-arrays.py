class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        k = n1 + n2 
        i = 0
        j = 0
        l = []
        while (i<n1 and j<n2):
            if nums1[i]<=nums2[j]:
                l.append(nums1[i])
                i += 1
            else:
                l.append(nums2[j])
                j += 1
        while i<n1:
            l.append(nums1[i])
            i += 1
        while j<n2:
            l.append(nums2[j])
            j += 1

        if k % 2 !=0:
            return float(l[k // 2])
        else:
            return (l[(k // 2) - 1] + l[k // 2]) / 2.0
        
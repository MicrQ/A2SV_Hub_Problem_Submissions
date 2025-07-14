# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)
        heap = [(nums1[0] + nums2[0], 0, 0)]
        seen = {(0, 0)}
        result = []

        while heap and k > 0:
            val, i, j = heappop(heap)
            result.append([nums1[i], nums2[j]])

            if i + 1 < n1 and (i + 1, j) not in seen:
                seen.add((i + 1, j))
                heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))

            if j + 1 < n2 and (i, j + 1) not in seen:
                seen.add((i, j + 1))
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

            k -= 1

        return result

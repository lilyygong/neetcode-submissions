from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        maxHeap = []
        heapq.heapify(maxHeap)
        res = []
        for num, count in count.items():
            heapq.heappush(maxHeap, (-count, num))
        while k > 0:
            tempCount, tempNum = heapq.heappop(maxHeap)
            res.append(tempNum)
            k -= 1
        return res

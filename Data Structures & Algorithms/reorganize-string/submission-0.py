from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""
        maxHeap = []
        prev = None
        heapq.heapify(maxHeap)
        count = Counter(s)
        for char, cnt in count.items():
            heapq.heappush(maxHeap, (-cnt, char))
        while maxHeap:
            tempCount, tempChar = heapq.heappop(maxHeap)
            res += tempChar
            if prev:
                heapq.heappush(maxHeap, prev)
            prev = (tempCount + 1, tempChar) if tempCount + 1 < 0 else None
        if prev and not maxHeap:
            return ""
        return res


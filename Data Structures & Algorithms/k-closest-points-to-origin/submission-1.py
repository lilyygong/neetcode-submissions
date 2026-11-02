class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            heapq.heappush(minHeap, (dist, x, y))
        while k > 0:
            tempDist, tempX, tempY = heapq.heappop(minHeap)
            res.append([tempX, tempY])
            k -= 1
        return res
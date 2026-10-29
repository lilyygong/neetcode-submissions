class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones) #maxHeap

        while len(stones) > 1:
            tempx = heapq.heappop(stones)
            tempy = heapq.heappop(stones)
            if tempx == tempy:
                continue
            elif -tempy < -tempx:
                tempx -= tempy
                heapq.heappush(stones, tempx)
        return 0 if not stones else -stones[0]
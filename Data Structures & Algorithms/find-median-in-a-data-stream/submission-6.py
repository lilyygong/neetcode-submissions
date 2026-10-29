class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -1 * num)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            tempMinPop = -1 * heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, tempMinPop)
        elif len(self.maxHeap) > len(self.minHeap) + 1:
            tempMaxPop = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, tempMaxPop)

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (self.minHeap[0] + (-1 * self.maxHeap[0])) / 2.0
        elif len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        else:
            return self.minHeap[0]
    
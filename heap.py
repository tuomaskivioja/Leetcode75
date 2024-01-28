# Merge K Sorted Lists
import heapq
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[ListNode]) -> ListNode:
    min_heap = []
    for l in lists:
        while l:
            heapq.heappush(min_heap, l.val)
            l = l.next
    dummy = ListNode(0)
    current = dummy
    while min_heap:
        current.next = ListNode(heapq.heappop(min_heap))
        current = current.next
    return dummy.next

# Top K Frequent Elements
def topKFrequent(nums: List[int], k: int) -> List[int]:
    # Create a frequency dictionary
    freq_dict = {}
    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    # Use a heap to find the k most frequent elements
    return heapq.nlargest(k, freq_dict.keys(), key=freq_dict.get)


# Find Median from Data Stream
class MedianFinder:
    def __init__(self):
        self.small = []  # Max heap
        self.large = []  # Min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if (self.small and self.large and
            (-self.small[0]) > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance the heaps
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2

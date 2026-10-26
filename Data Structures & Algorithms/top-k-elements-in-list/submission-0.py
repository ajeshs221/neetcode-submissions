import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts=Counter(nums)
        heap=[]
        for value,count in counts.items():
            if len(heap) < k:
                heapq.heappush(heap,(count,value))
            else:
                heapq.heappushpop(heap,(count,value))
        result=[]
        for i in heap:
            result.append(i[1])
        return result

                
        
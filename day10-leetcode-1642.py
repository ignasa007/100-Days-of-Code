# https://leetcode.com/problems/furthest-building-you-can-reach/

from typing import List
from heapq import heapify, heapreplace

class Solution:
    
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        heap = []
    
        for i in range(1, len(heights)):
            
            jump = heights[i] - heights[i-1]
            if jump > 0:
                
                if len(heap) < ladders:
                    heap.append(jump)
                    if len(heap) == ladders:
                        heapify(heap)
                    continue
                    
                if heap and jump > heap[0]:
                    jump = heapreplace(heap, jump)
                bricks -= jump
                if bricks < 0:
                    return i-1
                
        return i
            
            
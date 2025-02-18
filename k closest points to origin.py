#Back-end complete function Template for Python 3
import heapq


class Solution:

    def squared_distance(self, point: List[int]) -> int:
        return point[0]**2 + point[1]**2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for i, point in enumerate(points):
            distance = -self.squared_distance(point)  # Negate for max heap
            heapq.heappush(max_heap, (distance, i))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [points[i] for (_, i) in max_heap]

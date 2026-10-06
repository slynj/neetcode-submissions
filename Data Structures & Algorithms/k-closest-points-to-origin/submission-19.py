class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = defaultdict(list)
        res = []
        maxHeap = []

        for point in points:
            dist[(math.sqrt((point[0])**2 + (point[1])**2))].append(point)
        
        for d in dist.keys():
            for v in dist[d]:
                maxHeap.append(d)

        heapq.heapify_max(maxHeap)
        print(maxHeap)

        while len(maxHeap) > k:
            heapq.heappop_max(maxHeap)
        
        # print(maxHeap)
        
        for key in maxHeap:
            val = dist[key].pop()
            res.append(val)
        
        return res

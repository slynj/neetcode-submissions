class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        width, height = len(heights[0]), len(heights)
        pacific, atlantic = set(), set()

        def dfs(y, x, visit, h):
            if (y, x) in visit or y < 0 or y >= height or x < 0 or x >= width or h > heights[y][x]:
                return
            visit.add((y, x))
            dfs(y+1, x, visit, heights[y][x])
            dfs(y-1, x, visit, heights[y][x])
            dfs(y, x+1, visit, heights[y][x])
            dfs(y, x-1, visit, heights[y][x])

        for i in range(height):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, width - 1, atlantic, heights[i][width - 1])
        
        for i in range(width):
            dfs(0, i, pacific, heights[0][i])
            dfs(height - 1, i, atlantic, heights[height - 1][i])
        res =[]
        for pac in pacific:
            if pac in atlantic:
                res.append([pac[0],pac[1]])
        return res
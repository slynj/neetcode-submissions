class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if r < 0 or c < 0 or r >= row or c >= col or (r, c) in visit or prevHeight > heights[r][c]:
                return
            
            visit.add((r, c))

            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        
        for i in range(row):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, col-1, atl, heights[i][-1])
        
        for i in range(col):
            dfs(0, i, pac, heights[0][i])
            dfs(row-1, i, atl, heights[-1][i])
        
        res = []
        print(pac)
        print(atl)
        for item in pac:
            if item in atl:
                res.append(list(item))
        return res
        
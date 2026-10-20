class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, lst, prevHeight):
            if r < 0 or c < 0 or r >= row or c >= col or prevHeight > heights[r][c] or (r, c) in lst:
                return
            lst.add((r, c))

            dfs(r+1, c, lst, heights[r][c])
            dfs(r-1, c, lst, heights[r][c])
            dfs(r, c+1, lst, heights[r][c])
            dfs(r, c-1, lst, heights[r][c])

        for i in range(row):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, col-1, atl, heights[i][col-1])
        
        for i in range(col):
            dfs(0, i, pac, heights[0][i])
            dfs(row-1, i, atl, heights[row-1][i])
        res = []
        for cell in pac:
            if cell in atl:
                res.append([cell[0], cell[1]])
        return res

        


        
        


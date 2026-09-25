class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        idx = 0
        
        for r in board:
            col = []
            group = []
            rnorm = []

            for i in r:
                if i.isdigit():
                    rnorm.append(int(i))

            if len(set(rnorm)) != len(rnorm):
                return False
            for i in range(9):
                num = board[i][idx]
                if num.isdigit():
                    col.append(num)
            if len(set(col)) != len(col):
                return False
            mod = idx % 3
            div = idx // 3
            for i in range(3 * div, 3 * div +3):
                # 0 -> [0][0-2] [1][0-2] [2][0-2]
                # 1 -> [0][3-5] [1][3-5] [2][3-5]
                # 2 -> [0][6-8] [1][6-8] [2][6-8]
                # 3 -> [3][0-2] [4][0-2] [5][0-2]

                n1 = board[i][3 * mod]
                n2 = board[i][3 * mod + 1]
                n3 = board[i][3 * mod + 2]

                if n1.isdigit():
                    group.append(n1)
                if n2.isdigit():
                    group.append(n2)
                if n3.isdigit():
                    group.append(n3)

            if len(set(group)) != len(group):
                return False
            idx += 1
        return True


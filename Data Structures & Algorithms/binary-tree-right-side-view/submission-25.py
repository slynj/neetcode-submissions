# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root])

        while queue:
            length = len(queue)
            current_level = []
            for i in range(length):
                node = queue.popleft()
                if node:
                    current_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if current_level:
                res.append(current_level[-1])
        return res


        
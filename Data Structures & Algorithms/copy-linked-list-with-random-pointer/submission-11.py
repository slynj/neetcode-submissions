"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        copy_map = {}
        node = head
        
        while node:
            copy = Node(node.val)
            copy_map[node] = copy
            node = node.next
        
        node = head

        while node:
            copy = copy_map[node]
            if node.next:
                copy.next = copy_map[node.next]
            
            if node.random:
                copy.random = copy_map[node.random]

            node = node.next
        
        return copy_map[head]




        

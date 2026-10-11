class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.prev = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.nxt = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        prev = node.prev
        nxt = node.nxt

        prev.nxt = nxt
        nxt.prev = prev

        self.cache.pop(node.key)

    def insert(self, node):
        self.cache[node.key] = node

        prev = self.right.prev
        nxt = self.right

        prev.nxt = nxt.prev = node
        node.nxt = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = Node(key, self.cache[key].val)
            self.remove(self.cache[key])
            self.insert(node)
            
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.insert(node)

        if len(self.cache) > self.cap:
            self.remove(self.left.nxt)
        
        

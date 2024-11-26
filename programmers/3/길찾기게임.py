import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, x, n):
        self.x = x
        self.n = n
        self.left, self.right = None, None

class Tree:
    def __init__(self, n, x):
        self.root = Node(n, x)

    def insert(self, x, n):
        current = self.root

        while True:
            if current.x > x:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(x, n)
                    break
            elif current.x < x:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(x, n)
                    break
    
    def preorder(self):
        answer = []
        def _preorder(node):
            answer.append(node.n)
            if node.left:
                _preorder(node.left)
            if node.right:
                _preorder(node.right)
        _preorder(self.root)

        return answer
     
    def postorder(self):
        answer = []
        def _postorder(node):
            if node.left:
                _postorder(node.left)
            if node.right:
                _postorder(node.right)
            answer.append(node.n)
        _postorder(self.root)
        
        return answer
                        

def solution(nodeinfo):
    answer = []

    for node in nodeinfo:
        node.append(nodeinfo.index(node) + 1)
    
    nodeinfo.sort(key=lambda x: x[1], reverse=True)
    tree = Tree(nodeinfo[0][0], nodeinfo[0][2])

    nodeinfo.pop(0)
    for node in nodeinfo:
        tree.insert(node[0], node[2])
    
    answer.append(tree.preorder())
    answer.append(tree.postorder())

    return answer


print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
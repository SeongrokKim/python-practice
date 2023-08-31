import sys
sys.setrecursionlimit(10**6)

class Tree:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.data = None
        self.index = None
        
def solution(nodeinfo):
    answer = []
    new_node_info = []
    for i in range(len(nodeinfo)):
        new_node_info.append((i+1, nodeinfo[i][0], nodeinfo[i][1]))            
    new_node_info.sort(key=lambda x:(-x[2], x[1]))
    root = None
    for node in new_node_info:
        newTree = Tree()
        newTree.index = node[0]
        newTree.data = node[1]
        if root == None:
            root = newTree
        else:
            curTree = root
            while True:
                if curTree.data < newTree.data:
                    if curTree.right == None:
                        curTree.right = newTree
                        newTree.parent = curTree
                        break
                    else:
                        curTree = curTree.right
                else:
                    if curTree.left == None:
                        curTree.left = newTree
                        newTree.parent = curTree
                        break
                    else:
                        curTree = curTree.left
    pre = []
    post = []
    def findOrder(root, pre, post):
        pre.append(root.index)
        if root.left != None:
            findOrder(root.left, pre, post)
        if root.right != None:
            findOrder(root.right, pre, post)
        post.append(root.index)
    
    findOrder(root, pre, post)
    answer.append(pre)
    answer.append(post)
    return answer
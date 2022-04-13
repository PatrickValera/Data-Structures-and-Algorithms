class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class Tree:
    def createNode(self,data):
        return Node(data)
    def insertNode(self,node,data):
        if node is None:
            return self.createNode(data)
        if data<node.data:
            node.left=self.insertNode(node.left,data)
        else:
            node.right=self.insertNode(node.right,data)
        return node
    def inOrderPrint(self,root):
        if root is not None:
            self.inOrderPrint(root.left)
            print(root.data)
            self.inOrderPrint(root.right)

tree=Tree()
root=tree.createNode(5)
for num in [2,10,1,9,7,30]:
    tree.insertNode(root,num)

tree.inOrderPrint(root)

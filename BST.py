class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None  

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if data < current.data:  
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    current = current.left
            else:  
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    current = current.right

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")  
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")  
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")  


bst = BST()
elements = [45, 15, 79, 90, 10, 55, 12, 20, 50]

for elem in elements:
    bst.insert(elem)

print("\nInorder Traversal:")
bst.inorder(bst.root)  

print("\nPreorder Traversal:")
bst.preorder(bst.root)  

print("\nPostorder Traversal:")
bst.postorder(bst.root)  
class BSTNode:
    def __init__(self, data: int=None):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        pNew=BSTNode(data)
        if self.root is None:
            self.root=pNew
        else:
            current = self.root
            while current is not None:
                if data < current.data:
                    if current.left is None:
                        current.left = pNew
                        break
                    else:
                        current = current.left
                elif data > current.data:
                    if current.right is None:
                        current.right = pNew
                        break
                    else:
                        current = current.right
                else:
                    break
    def is_empty(self):
        return self.root is None
    def preorder(self,node):
        if node is not None:
            print(" ->",node.data,end="")
            self.preorder(node.left)
            self.preorder(node.right)
    def inorder(self,node):
        if node is not None:
            self.inorder(node.left)
            print(" ->",node.data,end="")
            self.inorder(node.right)
    def postorder(self,node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(" ->",node.data,end="")
    def traverse(self,node):
        if self.is_empty():
            print("This is an empty binary search tree.")
        else:
            print(f"Preorder:",end="")
            self.preorder(node)
            print(f"\nInorder:",end="")
            self.inorder(node)
            print(f"\nPostorder:",end="")
            self.postorder(node)
    def find_min(self,node):
        if node is None:
            self.is_empty()
        elif node.left is None:
            return node.data
        else:
            return self.find_min(node.left)
    def find_max(self,node):
        if node is None:
            self.is_empty()
        elif node.right is None:
            return node.data
        else:
            return self.find_max(node.right)
def main():
  my_bst = BST()
  for i in range(int(input())):
    my_bst.insert(int(input()))
  my_bst.traverse(my_bst.root)
  print("\nMax:", my_bst.find_max(my_bst.root))
  print("Min:", my_bst.find_min(my_bst.root))
main()
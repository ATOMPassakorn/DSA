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
    def preorder(self,node):
        if node is not None:
            print(" ->",node.data,end="")
            self.preorder(node.left)
            self.preorder(node.right)
def main():
  my_bst = BST()
  for i in range(int(input())):
    my_bst.insert(int(input()))
    
  print("Preorder:", end="")
  my_bst.preorder(my_bst.root)
main()
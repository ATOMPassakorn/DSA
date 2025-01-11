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
    def delete(self,data):
        if self.is_empty():
            print("Delete Error, " + str(data) + " is not found in Binary Search Tree.")
            return None
        parent = None
        current = self.root
        while current is not None and current.data != data:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right
        if current is None:
            print("Delete Error, " + str(data) + " is not found in Binary Search Tree.")
            return None
        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None
        elif current.right is None:
            if parent is None: 
                self.root = current.left
            elif parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
        elif current.left is None:
            if parent is None:
                self.root = current.right
            elif parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right
        else:
            max_node = self.find_max(current.left)
            self.delete(max_node)
            current.data = max_node
def main():
  my_bst = BST()
  while 1:
    text = input()
    if text == "Done":
      break
    condition, data = text.split(": ")
    if condition == "I":
      my_bst.insert(int(data))
    elif condition == "D":
      my_bst.delete(int(data))
    else:
      print("Invalid Condition")
  my_bst.traverse(my_bst.root)

main()
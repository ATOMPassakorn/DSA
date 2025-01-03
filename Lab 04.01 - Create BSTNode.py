class BSTNode:
    def __init__(self, data: int=None):
        self.data=int(data)
        self.left=None
        self.right=None
def main():
    p_new=BSTNode(input())
    print(p_new.data)
    print(p_new.left)
    print(p_new.right)
main()
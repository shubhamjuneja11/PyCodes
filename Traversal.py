class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.val=value

    def printInorder(root):
        if(root):
            printInorder(root.left)
            print(root.val)
            printInorder(root.right)

    def printPostorder(root):
        if(root):
            printPostorder(root.left)
            printPostorder(root.right)
            print(root.val)

    def printPreorder(root):
        if(root):
            print(root.val)
            printPreorder(root.left)
            printPreorder(root.right)
    if __name__=="__main__":
        n=Node(1);
        print('h')

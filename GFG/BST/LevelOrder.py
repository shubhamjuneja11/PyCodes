class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def getHeight(root):
    if root is None:
        return 0
    else:
        lheight=getHeight(root.left)
        rheight=getHeight(root.right)
        if lheight>rheight:
            return lheight+1
        else :
            return rheight+1
def printLevel(root):
    height=getHeight(root)
    for i in range(1,height+1):
        printGivenLevel(root,i)
def printGivenLevel(root,level):
    if root is None:
        return
    if level==1:
        print(root.value)
    elif level>1:
        printGivenLevel(root.left,level-1)
        printGivenLevel(root.right,level-1)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Level order traversal of binary tree is -")
printLevel(root)

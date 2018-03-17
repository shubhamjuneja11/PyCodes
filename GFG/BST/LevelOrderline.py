class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printLevelOrderLine(root):
    queue=[]
    queue.append(root)
    while(1):
        size=len(queue)
        if size==0:
            break
        while(size>0):
            node=queue.pop(0)
            print(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            size-=1
        print()
root =  Node(1);
root.left =  Node(2);
root.right = Node(3);
root.left.left =  Node(4);
root.left.right =  Node(5);
root.right.right =  Node(6);
printLevelOrderLine(root)

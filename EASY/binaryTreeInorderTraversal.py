


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
        if not root :
            return []
        arr = auxInorder(root, [])
        return arr

def auxInorder(root, arr):
    if root.left == None:
        arr.append(root.val)
        if root.right != None :
            auxInorder(root.right, arr)
    else :
        auxInorder(root.left, arr)
        arr.append(root.val)
        if root.right != None:
            auxInorder(root.right, arr)
    
    return arr
    

root = TreeNode()
root.val = 1
root.right = TreeNode()
root.right.val = 2
root.right.left = TreeNode()
root.right.left.val = 3

print(inorderTraversal(root))

# taken from the internet
# Inorder tree traversal (Left - Root - Right)
def inorderTraversal(root):
    if not root:
        return
    inorderTraversal(root.left)
    print(root.val, end=" ")
    inorderTraversal(root.right)

root = TreeNode()
root.val = 1
root.right = TreeNode()
root.right.val = 2
root.right.left = TreeNode()
root.right.left.val = 3

print(inorderTraversal(root))



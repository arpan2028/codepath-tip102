class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def check_balanced(root):
    if not root:
        return True
    
    while root:
        return check_balanced(root.left) - check_balanced(root.right) <= 1

    
root = [3,9,20,15,7]   
print(check_balanced(root))
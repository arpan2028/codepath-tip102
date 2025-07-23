from collections import deque


# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)


# root = TreeNode("Trunk")
# mc = TreeNode("Mcintosh")
# gs = TreeNode("Granny Smith")
# root.left = mc
# root.right = gs
# fuji = TreeNode("Fuji")
# opal = TreeNode("Opal")
# mc.left = fuji
# mc.right = opal
# crab = TreeNode("Crab")
# gala = TreeNode("Gala")
# gs.left = crab
# gs.right = gala

# print_tree(root)


def calculate_yield(root):
    # if there is no root
    if root is None or root.left is None or root.right is None:
        return 0
    # assign left and right values
    left_val = root.left.val
    right_val = root.right.val
    # if else statement to determine symbol
    if root.val == "+":
        return left_val + right_val
    elif root.val == "-":
        return left_val - right_val
    elif root.val == "*":
        return left_val * right_val
    else:
        return left_val / right_val


apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

print(calculate_yield(apple_tree))


def right_vine(root):
    result = []
    result.append(root.val)
    while root.right:
        result.append(root.right.val)
        root = root.right
    return result


def right_vine_recur(root):
    if not root.right:
        return [root.val]
    return [root.val] + right_vine_recur(root.right)


ivy1 = TreeNode(
    "Root",
    TreeNode("Node1", TreeNode("Leaf1")),
    TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")),
)

print(right_vine_recur(ivy1))
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


def count_leaves(root):
    if root is None:
        return 0
    elif root.right is None and root.left is None:
        return 1
    return count_leaves(root.right) + count_leaves(root.left)


print(count_leaves(ivy1))


def survey_tree(root):
    if root is None:
        return []
    else:
        return survey_tree(root.left) + survey_tree(root.right) + [root.val]


magnolia = TreeNode(
    "Root",
    TreeNode("Node1", TreeNode("Leaf1")),
    TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")),
)

print(survey_tree(magnolia))

"""
You are given a binary tree.
Write a function that can return the inorder traversal of node values.
Example:
Input:
   3
    \
     1
    /
   5
Output: [3,5,1]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    # create an inner helper function
    def helper(root, result):
        # if root exists
        if root:
            # call helper on the left of the root, passing the result list along
            helper(root.left, result)
            # in order thing!
            # append roots value to the result list
            result.append(root.val, result)
            # call the helper on the right of the root, passing the result list along
            helper(root.right)
    
    result = []
    helper(root, result)
    
    return result

# iterative solution
def inorder_traversal(root):
    # hold the result
    result = []
    # make a stack
    stack = []

    # iterate
    while True:
        # while the root node is not none
        while root: 
            # append the root to the stack
            stack.append(root)
            # traverse to the left of the root
            root = root.left

            # if there is no stack
            if not stack:
                # return the result
                return result
            # pop the stack on to a node variable
            node = stack.pop()
            # append the nodes value to the result list
            result.append(node.val)
            # traverse to the right of the node
            root = root.right

"""Allision solution"""
# def inorder_traversal(root):
#     if not root:
#         return []
#     left = inorder_traversal(root.left)
#     right = inorder_traversal(root.right)
#     return left + [root.val] + right




t1 = TreeNode(3)
t1.right = TreeNode(1)
t1.right.left = TreeNode(5)

print(inorder_traversal(t1))
from collections import deque

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def traverse_tree(self, node, level):
        # print(node.val)
        if len(self.ans) < level:
            self.ans.append([])
        self.ans[level-1].append(node.val)
        if node.left:
            self.traverse_tree(node.left, level+1)
        if node.right:
            self.traverse_tree(node.right, level+1)

    def levelOrder(self, A):
        self.ans = []
        self.traverse_tree(A, 1)
        return self.ans

    def levelOrder_2(self, A):
        current_level = deque([A])
        next_level = deque()
        levels = [[A.val]]
        while current_level:
            node = current_level.popleft()
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            if not current_level:
                if next_level:
                    levels.append([n.val for n in next_level])
                current_level = next_level
                next_level = deque()
        return levels

# Test code
assert Solution().solve('') == ''

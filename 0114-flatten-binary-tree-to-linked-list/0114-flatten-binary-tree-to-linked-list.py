class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        stack = [root]

        while stack:
            node = stack.pop()

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

            if stack:
                node.right = stack[-1]

            node.left = None
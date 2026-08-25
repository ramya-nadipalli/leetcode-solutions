class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, remaining, path):
            if node is None:
                return

            path.append(node.val)
            remaining -= node.val

            # Check only at a leaf
            if node.left is None and node.right is None:
                if remaining == 0:
                    result.append(path.copy())
            else:
                dfs(node.left, remaining, path)
                dfs(node.right, remaining, path)

            # Backtrack
            path.pop()

        dfs(root, targetSum, [])
        return result
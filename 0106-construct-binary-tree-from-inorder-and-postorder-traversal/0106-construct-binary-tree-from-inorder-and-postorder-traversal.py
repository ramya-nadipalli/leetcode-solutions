class Solution:
    def buildTree(self, inorder, postorder):
        pos = {v: i for i, v in enumerate(inorder)}
        post = len(postorder) - 1

        def build(left, right):
            nonlocal post

            if left > right:
                return None

            root_val = postorder[post]
            post -= 1

            root = TreeNode(root_val)

            idx = pos[root_val]

            root.right = build(idx + 1, right)
            root.left = build(left, idx - 1)

            return root

        return build(0, len(inorder) - 1)
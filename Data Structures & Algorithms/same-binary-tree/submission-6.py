# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if p and not q:
            return False
        
        if q and not p:
            return False
        
        if p.right and not q.right:
            return False
        
        if p.left and not q.left:
            return False

        if p.val != q.val:
            return False
            
        pr, pl = p.right, p.left
        qr, ql = q.right, q.left

        if pr and qr:
            if pr.val != qr.val:
                return False
        
        if pl and ql:
            if pl.val != ql.val:
                return False

        return self.isSameTree(pr, qr) and self.isSameTree(pl, ql)
        
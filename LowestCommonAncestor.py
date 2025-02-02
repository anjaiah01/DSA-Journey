class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if the root is None, or if root matches either p or q, return root
        if root == None or root == p or root == q:
            return root
        
        # Recursively find LCA in the left subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        
        # Recursively find LCA in the right subtree
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are non-null, root is the LCA
        if left != None and right != None:
            return root
        
        # If only one side returns a node, return that node (p and q are in the same subtree)
        return left if left != None else right




# Approach:

# If root is null or if root is x or if root is y then return root
# Made a recursion call for both
# i) Left subtree 

# ii)Right subtree

# Because we would find LCA in the left or right subtree only.

# If the left subtree recursive call gives a null value that means we haven’t found LCA in the left subtree, which means we found LCA on the right subtree. So we will return right.
# If the right subtree recursive call gives null value, that means we haven’t found LCA on the right subtree, which means we found LCA on the left subtree. So we will return left .
#  If both left & right calls give values (not null)  that means the root is the LCA.
# Let’s take an example and will try to understand the approach more clearly:

# LCA of (x,y) = > (4,5) = ? (from above given example)
# Root is 1 which is not null and x,y is not equal to root, So the 1st statement in approach  will not execute.
# i) Call left subtree, While calling recursively it will find 4 and this call will return 4 to its parent 
# Point to Note: At present, the root is 2 ( Look at below recursion tree for better understanding)

# i) Call the right subtree ( i.e right of 2), While calling recursively it will find 5  and this call will return 5 to its parent.

# Now the left recursive  call returns value (not null) i.e 4 and also the right recursive call returns value (not null) i.e 5 to its root ( at present root is 2) , and this 2 will return itself to its root i.e to 1 (main root).
# Point to Note: At present, the root is 1 ( Look at below recursion tree for better understanding)

# Now, the left subtree gives a value i.e 2.
# Right recursive call will give null value .because x,y are not present in the right subtree.
# As we know if the right recursive call gives null then we return the answer which we got from the left call, So we will return 2.
#  Hence LCA of (4,5) is 2.

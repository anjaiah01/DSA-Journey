#Traversals of Binary tree without Using recurssion ---> Morris Algo

# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# Return a list containing the inorder traversal of the given tree
class Solution:
    def inOrder(self, root):
        inorder = []
        curr = root
        while curr != None:
            if curr.left == None:
                inorder.append(curr.data)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right != None and prev.right != curr:
                    prev = prev.right
                
                if prev.right == None:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    inorder.append(curr.data)
                    curr = curr.right
        return inorder


    # Return a list containing the preorder traversal of the given tree
    def preOrder(self, root):
        preorder = []
        curr = root
        
        while curr != None:
            
            if curr.left == None:
                preorder.append(curr.data)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right != None and prev.right != curr:
                    prev = prev.right
                if prev.right == None:
                    prev.right = curr
                    preorder.append(curr.data)
                    curr = curr.left
                else:
                    prev.right = None
                    curr = curr.right
        return preorder

    def postOrder(self, node):
        # initializing an empty list to store the postorder traversal
        ans = []
        # initializing an empty stack
        s = []

        # checking if the given node is None, if yes then returning the empty list
        if node == None:
            return ans

        # pushing the root node into the stack
        s.append(node)
        # initializing a variable for keeping track of the previous visited node
        prev = None

        # loop until the stack becomes empty
        while len(s) > 0:
            # getting the top node from the stack
            current = s[-1]

            # if the current node is the first node or the previous node is the left child of the current node or the previous node is the right child of the current node
            if ((not prev) or (prev.left == current)
                    or (prev.right == current)):
                # if the current node has a left child, then push it into the stack
                if current.left:
                    s.append(current.left)
                # if the current node does not have a left child but has a right child, then push it into the stack
                elif current.right:
                    s.append(current.right)
                # if the current node does not have any child, then remove it from the stack and add its data to the answer list
                else:
                    s.pop()
                    ans.append(current.data)
            # if the previous node is the left child of the current node
            elif current.left == prev:
                # if the current node has a right child, then push it into the stack
                if current.right:
                    s.append(current.right)
                # if the current node does not have a right child, then remove it from the stack and add its data to the answer list
                else:
                    s.pop()
                    ans.append(current.data)
            # if the current node has a right child
            elif current.right:
                # remove the current node from the stack and add its data to the answer list
                s.pop()
                ans.append(current.data)

            # updating the previous node
            prev = current

        # returning the postorder traversal
        return ans

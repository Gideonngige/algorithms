def invertTree(root, self):
    #Base case: if root is None, return None
    if not root:
        return None
    
    #recursively invert left and right subtrees
    left = self.invertTree(root.left)
    right = self.invertTree(root.right)
    
    #swap left and right children
    root.left = right
    root.right = left
    
    #return the new root
    return root

root = [4, 2, 7, 1, 3, 6, 9]
print(invertTree(root))
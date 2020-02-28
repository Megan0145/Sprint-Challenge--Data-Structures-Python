class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if new value will fall on RHS of value of current BST (is it MORE than OR EQUAL to the root node of the current BST)
        if value >= self.value:
            # if current BST does not have a right node
            if not self.right:
                # add new subtree to the right 
                self.right = BinarySearchTree(value)
                return
            # else recur insert function, this time passing the right node of the current node as the root node (ie self now == self.right)
            else:
                return self.right.insert(value)
        # else new value must fall on LHS of BST (it's LESS than value of the current BST)
        else:
            # if current BST does not have a left node
            if not self.left:
                # add new subtree to the left
                self.left = BinarySearchTree(value)  
                return
            # else recur insert function, this time passing the left node of the current BST as the root node (ie self now == self.left)
            else:
                return self.left.insert(value) 

    
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # base case: if value of current node is equal to the target value we're looking for
        # BST contains target -> return True
        if self.value == target:
            return True

        # if target is more than the value at the current node we want to continue onto the next node to compare on the RHS
        # can only do that is current node has node to RHS     
        elif target > self.value and self.right:
            # if both conditions true recur function by calling function on the node to the RHS of the current node
            return self.right.contains(target)

        # if target is more than the value at the current node we want to continue onto the next node to compare on the RHS
        # can only do that is current node has node to RHS       
        elif target < self.value and self.left:
            # if both conditions true recur function by calling function on the node to the RHS of the current node
            return self.left.contains(target)
        
        # else we've come to the very last node that the target may possibly reside, return False
        else:
            return False  
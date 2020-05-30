class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                new_node = BSTNode(value)
                self.right = new_node
        else:
            if self.left:
                self.left.insert(value)
            else:
                new_node = BSTNode(value)
                self.left = new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        
        else:
            return self.left.contains(target) if self.left else False

    # Return the maximum value found in the tree
    def get_max(self):
        max = self.value
        if self.right:
            return self.right.get_max()
        else:
            return max


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)
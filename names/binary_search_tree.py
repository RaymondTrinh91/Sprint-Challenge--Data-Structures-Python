# import sys
# sys.path.append('./queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #* Check if value is smaller than Node
        if value < self.value:
            #* Check if node exists
            #* If node exists, call insert on that node
            if self.left is not None:
                self.left.insert(value)
            #* If there is no Node, create a new one
            else:
                self.left = BinarySearchTree(value)
        #* If value is greater than or equal to Node
        #* Do the same
        else:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #* If target is found return True
        if target == self.value:
            return True
        #* If target is smaller than Node
        if target < self.value:
            #* If there are no more nodes
            #* Return False
            if self.left == None:
                return False
            #* If there are more nodes
            #* Continue checking left side
            else:
                return self.left.contains(target)
        #* If target is greater than value
        #* Do the same
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # *Go right until you cannot
        #* Return highest value
        if self.right:
            return self.right.get_max()
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        #* If there is a left node
        #* Go left calling the function on the node
        if self.left:
            self.left.for_each(cb)
        #* If there is a right node
        #* Do the same
        if self.right:
            self.right.for_each(cb)
        #* Use Callback on node
        cb(self.value)

    # # DAY 2 Project ---  --------------------

    # # Print all the values in order from low to high
    # # Hint:  Use a recursive, depth first traversal
    # def in_order_print(self, node):
    #     storage = Stack()
    #     storage.push(node)
    #     while storage.len() > 0:
    #         head = storage.pop()
    #         if head.left:
    #             self.in_order_print(head.left)
    #         if head.right:
    #             storage.push(head.right)
    #         print(head.value)


    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     storage = Queue()
    #     storage.enqueue(node)
    #     while storage.len() > 0:
    #         head = storage.dequeue()
    #         print(head.value)
    #         if head.left:
    #             storage.enqueue(head.left)
    #         if head.right:
    #             storage.enqueue(head.right)
            
            

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
    #     storage = Stack()
    #     storage.push(node)
    #     while storage.len() > 0:
    #         head = storage.pop()
    #         print(head.value)
    #         if head.left:
    #             storage.push(head.left)
    #         if head.right:
    #             storage.push(head.right)

    # # STRETCH Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     storage = Stack()
    #     storage.push(node)
    #     while storage.len() > 0:
    #         head = storage.pop()
    #         print(head.value)
    #         if head.left:
    #             self.pre_order_dft(head.left)
    #         if head.right:
    #             self.pre_order_dft(head.right)

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     storage = Stack()
    #     storage.push(node)
    #     while storage.len() > 0:
    #         head = storage.pop()
    #         if head.left:
    #             self.post_order_dft(head.left)
    #         if head.right:
    #             self.post_order_dft(head.right)
    #         print(head.value)


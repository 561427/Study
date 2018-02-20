#
# BST.py
#
# Written by: Mitch A. Modin
#
import unittest

class Node:
    """Node class for BST.""""
    def __init__(self, Val):
        self.Val = Val
        self.Left = None
        self.Right = None

class BST:
    """Binary Search Tree."""
    def __init__(self):
        self.Head = None

    def insert(self, Val):
        """Insert new value."""
        if self.Head is not None:
            return self.insertNode(self.Head, Val)
        else:
            self.Head = Node(Val)
            return True

    def insertNode(self, MyNode, Val):
        """Recursive approach to insert new value."""
        if MyNode is not None:
            if Val < MyNode.Val:
                if MyNode.Left is not None:
                    self.insertNode(MyNode.Left, Val)
                else:
                    MyNode.Left = Node(Val)
                    return True
            elif Val > MyNode.Val:
                if MyNode.Right is not None:
                    self.insertNode(MyNode.Right, Val)
                else:
                    MyNode.Right = Node(Val)
                    return True
            else:
                return False

    def print(self):
        """Print In-Order traversal."""
        if self.Head is not None:
            self.printAll(self.Head)

    def printAll(self, MyNode):
        """Recursive approach to print In-Order traversal."""
        if MyNode.Left is not None:
            self.printAll(MyNode.Left)
        print(MyNode.Val)
        if MyNode.Right is not None:
            self.printAll(MyNode.Right)

    def height(self):
        """Obtain height of tree."""
        if self.Head is not None:
            return self.getHeight(self.Head)
        else:
            return 0

    def getHeight(self, MyNode):
        """Recursive approach to obtain height."""
        if MyNode is None:
            return 0
        else:
            return 1 + max(self.getHeight(MyNode.Left),self.getHeight(MyNode.Right))



class Test_BST(unittest.TestCase):
    def setUp(self):
        self.B = BST()

    def test_insert_new_value(self):
        """Test adding value to tree."""
        self.assertTrue(self.B.insert(7))

    def test_insert_existing_value(self):
        """Test adding existing value to tree."""
        self.B.insert(5)
        self.assertFalse(self.B.insert(5))

    def test_height(self):
        """Test obtaining height of tree."""
        self.B.insert(7)
        self.B.insert(3)
        self.B.insert(4)
        self.B.insert(2)
        self.B.insert(10)
        self.assertEqual(3,self.B.height())

# Standard boilerplate
def main():
    unittest.main()
if __name__ == "__main__":
    main()


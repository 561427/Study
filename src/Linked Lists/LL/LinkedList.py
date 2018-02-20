#
# ReverseLinkedList.py
#
#

class Node:
    def __init__(self,Val):
        self.Val = Val
        self.Next = None


class LinkedList:
    def __init__(self):
        self.Head = None


    def insert(self, Val):
        if self.Head is None:
            self.Head = Node(Val)
        else:
            self.insertNode(self.Head, Val)

    def insertNode(self, MyNode, Val):
        if MyNode.Next is not None:
            self.insertNode(MyNode.Next,Val)
        else:
            MyNode.Next = Node(Val)

    def printAll(self):
        if self.Head is not None:
            self.printAllNodes(self.Head)

    def printAllNodes(self,MyNode):
        print(MyNode.Val)
        if MyNode.Next is not None:
            self.printAllNodes(MyNode.Next)

    def reverse(self):
        if self.Head is not None:
            self.reverseList(self.Head, None)

    def reverseList(self, Curr, Prev):
        if Curr.Next is None:
            self.Head = Curr
            Curr.Next = Prev
            return
        NextNode = Curr.Next
        Curr.Next = Prev
        self.reverseList(NextNode, Curr)



L = LinkedList()
for i in range(10):
    L.insert(i)

L.reverse()
L.printAll()
        
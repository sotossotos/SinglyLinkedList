class Node:
    def __init__(self,value=None,nextNode=None):
        self.value=value
        self.nextNode=nextNode

class SinlgeLinkedList:
    def __init__(self,node=None):
        self.list=node
        self.size=0
    def addNodeTop(self,value):
        newNode=Node(value)
        newNode.nextNode=self.list
        self.list=newNode
        self.size+=1
    def addNodeBottom(self,value):
        newNode=Node(value)
        if self.list==None:
            self.addNodeTop(value)
            return
        head=self.list
        while head:
            previous=head
            head=head.nextNode
        previous.nextNode=newNode
        self.size+=1
        return
    def printListValues(self):
        head=self.list
        print(f"This is a List of size {self.size}")
        while head:
            print(f"the value is {head.value}")
            head=head.nextNode
        return
    def search (self,value):
        head=self.list
        while head:
            if head.value==value:
                return head
            else:
                head=head.nextNode
        return Node()
    def reverseList(self):
        head=self.list
        previous=None
        while head:
            temp_head=head
            head=head.nextNode
            temp_head.nextNode=previous
            previous=temp_head
        self.list=previous
        
        

    def delete(self,value):
        head=self.list
        previous=None
        while head:
            if head.value==value:
                if previous is None:
                    self.list=head.nextNode
                else:
                    
                    previous.nextNode=head.nextNode
                return
            else:
                previous=head
                head=head.nextNode
    def replaceNodeValue(self,newValue,value):
        node=self.search(value)
        node.value=newValue


class LinkedList:
    __slots__ = {'head'}

    def __init__(self):
        self.head = None

    class Node:
        __slots__ = {'next', 'value'}

        def __init__(self, val, nxt = None):
            self.value = val
            self.next = nxt

    def add(self, val):
        if self.head == None:
            self.head = self.Node(val)
        else:
            curr = self.head
            while(curr.next != None):
                curr = curr.next
            curr.next = self.Node(val)

    def remove(self, val):
        if self.head == None:
            return
        if self.head.value == val:
            self.head = self.head.next
        else:
            curr = self.head.next
            prev = self.head
            while(curr!= None ):
                if (curr.value == val):
                    break
                prev = curr
                curr = curr.next
            prev.next = curr.next

    def addAtIndex(self, index, val):
        if self.head == None:
            return
        if index == 0:
            temp = self.head
            self.head = self.Node(val)
            self.head.next = temp
        else:
            curr = self.head.next
            prev = self.head
            idx = 1
            while ( idx<index and curr!=None):
                prev = curr
                curr = curr.next
                idx += 1
            if idx != index :
                return
            temp = curr
            prev.next = self.Node(val)
            prev.next.next = temp

    def removeAtIndex(self, index):
        if self.head == None:
            return
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            idx = 0
            while(idx<index-1 and curr.next != None):
                curr = curr.next
                idx += 1
            if idx != index-1:
                return
            curr.next = curr.next.next

    def __str__(self):
        if self.head == None:
            return
        listrep = []
        rep = ""
        curr = self.head
        while curr != None:
            listrep.append(str(curr.value))
            rep = rep + " " + str(curr.value)
            curr = curr.next
        return " -> ".join(listrep)


def main():
    l1 = LinkedList()
    l1.add(5)
    l1.add(15)
    l1.add(12)
    l1.add(20)
    print(l1)
    l1.remove(12)
    print(l1)
    l1.addAtIndex(1,10)
    print(l1)
    l1.addAtIndex(0,0)
    print(l1)
    l1.removeAtIndex(0)
    print(l1)
    l1.addAtIndex(10,1)
    print(l1)
    l1.removeAtIndex(3)
    print(l1)



main()
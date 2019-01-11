class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SList:
    def __init__(self, value):
        node = Node(value)
        self.head = node

    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = node
        return self

    def removeNode(self, value):
        runner = self.head
        if runner.value == value:
            self.head = runner.next
        while (runner.next != None):
            prev_runner = runner
            runner = runner.next
            if runner.value == value:
                if runner.next == None:
                    prev_runner.next = None
                else:
                    prev_runner.next = runner.next
        return self

    def printAllValues(self, msg=""):
        runner = self.head
        print("\n\nhead points to ", id(self.head))
        print("Printing the values in the list ---", msg, "---")
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next
        print(id(runner), runner.value, id(runner.next))
        return self

    def displayList(self):
        elems = []
        runner = self.head
        while runner.next != None:
            elems.append(runner.value)
            runner = runner.next
        elems.append(runner.value)
        print(elems)
        return self


print("\n\n\n\n================== START OF THE PROGRAM ================")
list = SList(5)
list.addNode(7).addNode(9).addNode(1).addNode(8).printAllValues("Attemp 1")
# list.addNode(9)
# list.addNode(1)
list.removeNode(5).removeNode(9).removeNode(8).printAllValues("Attemp 1")
# list.removeNode(9)
# list.removeNode(1)
# list.printAllValues("Attemp 1")
# list.displayList()

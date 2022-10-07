class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;

class LinkedList:
    def __init__(self):
        self.head = None;
        self.size = 0;
        
    def size(self):
        return self.size;
        
    # O(1)
    def append(self, data):
        newNode = Node(data);
        
        if (self.head == None):
            self.head = newNode;
            return;
        
        newNode.next = self.head;
        self.head = newNode;
        self.size += 1;
    
    # O(n)
    def traverse(self):
        currentNode = self.head;
        
        self.traverseRecursively(currentNode);
        
    # O(n)
    def traverseRecursively(self, node):
        
        if (node == None):
            print("NULL");
            return;
        
        print(node.data, end="->");
        
        self.traverseRecursively(node.next);
      
    # O(n^2)  
    def sort(self):
        head = self.head;
        
        self.sortRecursively(head, head.next);
        
    # O(n^2)  
    def sortRecursively(self, firstNode, secondNode):
        
        if (firstNode.next == None):
            return;
        
        if (firstNode.data > secondNode.data):
            temp = firstNode.data;
            firstNode.data = secondNode.data;
            secondNode.data = temp;
        
        if (secondNode.next == None):
            firstNode = firstNode.next;
            secondNode = firstNode;
            
        self.sortRecursively(firstNode, secondNode.next);
    

class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;

class LinkedList:
    def __init__(self):
        self.head = None;
        
    # O(1)
    def append(self, data):
        newNode = Node(data);
        
        if (self.head == None):
            self.head = newNode;
            return;
        
        newNode.next = self.head;
        self.head = newNode;
    
    # O(n)
    def traverse(self):
        currentNode = self.head;
        
        while (currentNode != None):
            print(currentNode.data, end='->');
            
            currentNode = currentNode.next;
            
        print("NULL")
      
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
        
                 
linkedList = LinkedList();

linkedList.append(7);
linkedList.append(6);
linkedList.append(2); 
linkedList.append(3); 
linkedList.append(4); 
linkedList.append(5);
linkedList.append(1); 

linkedList.traverse();

linkedList.sort();

linkedList.traverse();
 

        
        

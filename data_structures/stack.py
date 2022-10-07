class Stack:
    def __init__(self):
        self.array = [];
      
    # O(1)  
    def push(self, data):
        self.array.append(data);
    
    # O(1)  
    def pop(self):
        if (self.empty()):
            return;
        
        return self.array.pop();
        
    # O(1)
    def peak(self):
        if (self.empty()): 
            return;
        
        return self.array[len(self.array) - 1];
    
    # O(1)
    def empty(self):
        return len(self.array) == 0;
    
    # O(n)
    def print(self):
        if (self.empty()):
            print("vazia", end=" > ");
        
        auxStack = Stack();
        
        while (not self.empty()):
            data = self.pop();
            auxStack.push(data);
        
        while (not auxStack.empty()):
            data = auxStack.pop();
            print(str(data), end=" > ");
            self.push(data);
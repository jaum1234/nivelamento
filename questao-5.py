class Stack:
    def __init__(self):
        self.array = [];
        
    def push(self, data):
        self.array.append(data);
        
    def pop(self):
        if (self.empty()):
            return;
        
        return self.array.pop();
        
    def peak(self):
        if (self.empty()): 
            return;
        
        return self.array[len(self.array) - 1];
    
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
            
stack = Stack();

def menu():
    
    print("Menu: ");
    print("1. página 1");
    print("2. página 2");
    print("3. página 3");
    print("4. voltar");
    print();
    print("5. sair");
    print();
    
    while (True):
        
        option = float(input("Selecione um item do menu: "));
        
        if (option == 1):
            stack.push("Página 1");
        elif (option == 2):
            stack.push("Página 2");
        elif (option == 3):
            stack.push("Página 3");
        elif (option == 4):
            stack.pop();
        else:
            break;
        
        print(stack.print());
        
menu();
    
from data_structures.stack import Stack
            
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
    
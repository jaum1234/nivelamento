from data_structures.stack import Stack;

# Resposta: Para realizarmos esta operação, inserimos a palavra numa pilha, uma letra em cada espaço, e depois retiramos todas as letras da pilha. Nessa estrutura de dados, os elementos seguem a lógica "First in, last out". 

# Exemplo: Ao inserirmos a palavra "BALÃO", após retirar cada caracter, a palavra estará na seguinte forma:
# O Ã L A B

# p.s.: exercicio 6 lista 1 (EDD1)

stack = Stack();

sentence = "Hello, world!";

for letter in sentence:
    stack.push(letter);
    
reversedSentence = "";

while (not stack.empty()):
    reversedSentence += stack.pop()


print(reversedSentence);
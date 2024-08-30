# Projeto de Estruturas de Dados

Este projeto demonstra o uso de três abordagens diferentes para trabalhar com listas encadeadas em Python: arrays, listas encadeadas (linked lists) e a classe `deque` do módulo `collections`. O código fornece exemplos de como criar, manipular e exibir esses tipos de dados.

## Descrição

O projeto contém três exemplos principais:

1. **Array**:
   - Utiliza o módulo `array` para criar e manipular um array de inteiros.
   - Exemplos de operações realizadas: inserção de um elemento, remoção de um elemento e acesso a um elemento específico.

2. **Lista Encadeada (Linked List)**:
   - Implementa uma lista encadeada com classes `Node` e `LinkedList`.
   - Inclui operações como adicionar um nó no final da lista, remover um nó com um valor específico e exibir todos os elementos da lista.

3. **Lista Encadeada com `deque`**:
   - Utiliza a classe `deque` do módulo `collections` para criar e manipular uma lista encadeada.
   - Exemplos de operações realizadas: inserção de elementos, remoção do primeiro e do último elemento, e inserção no início da lista.

## Estrutura do Código

### Manipulação de Array
```python
import array as arr

# Criando um array de inteiros
numeros_array = arr.array('i', [10, 20, 30, 40, 50])

# Acessando o terceiro elemento (index 2)
print(f"Elemento no índice 2: {numeros_array[2]}")

# Inserindo um novo elemento no final
numeros_array.append(60)
print(f"Array após inserção: {numeros_array}")

# Removendo o segundo elemento (index 1)
numeros_array.pop(1)
print(f"Array após remoção: {numeros_array}")

print("#" * 30)
print("         LinkedList:")
print("#" * 30)

```python


### Classe para representar a linked list
```python

class LinkedList:
    def __init__(self):
        self.head = None  # Início da lista

    # Método para adicionar um nó no final da lista
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    # Método para remover o primeiro nó com o valor especificado
    def remove(self, data):
        current_node = self.head

        if current_node is not None:
            if current_node.data == data:
                self.head = current_node.next
                current_node = None
                return

        prev_node = None
        while current_node is not None:
            if current_node.data == data:
                break
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev_node.next = current_node.next
        current_node = None

    # Método para exibir os elementos da lista
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

```python

### Lista Encadeada com `deque`
```python

from collections import deque

# Criando uma linked list usando deque
linked_list = deque()

# Adicionando elementos no final da linked list
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)

# Exibindo a linked list
print("Linked List após inserções:")
print(linked_list)

# Removendo o primeiro elemento
linked_list.popleft()
print("\nLinked List após remover o primeiro elemento:")
print(linked_list)

# Removendo o último elemento
linked_list.pop()
print("\nLinked List após remover o último elemento:")
print(linked_list)

# Inserindo no início da linked list
linked_list.appendleft(5)
print("\nLinked List após inserir 5 no início:")
print(linked_list)


import array as arr

# Criando um array de inteiros
numeros_array = arr.array('i', [10, 20, 30, 40, 50])

# Acessando o terceiro elemento (index 2)
print(f"Elemento no índice 2: {numeros_array[2]}")  # Saída: 30

# Inserindo um novo elemento no final
numeros_array.append(60)
print(f"Array após inserção: {numeros_array}")

# Removendo o segundo elemento (index 1)
numeros_array.pop(1)
print(f"Array após remoção: {numeros_array}")

print("#" * 30)
print("         LinkedList:")
print("#" * 30)

# Classe para representar um nó da linked list
class Node:
    def __init__(self, data):
        self.data = data  # Dado do nó
        self.next = None  # Ponteiro para o próximo nó

# Classe para representar a linked list
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

# Criando uma linked list e adicionando elementos
numeros_linked_list = LinkedList()
numeros_linked_list.append(10)
numeros_linked_list.append(20)
numeros_linked_list.append(30)
numeros_linked_list.append(40)
numeros_linked_list.append(50)

# Exibindo a lista
print("Linked List antes da remoção:")
numeros_linked_list.display()

# Removendo um elemento
numeros_linked_list.remove(20)
print("Linked List após a remoção:")
numeros_linked_list.display()


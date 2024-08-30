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

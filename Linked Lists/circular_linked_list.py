# Circular Linked List
# In a circular linked list, the tail node points to the head of the
#linked list instead of poiting to null

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class CircularLinkedList:
	def __init__(self):
		self.head = None

	def prepend(self, data):
		new_node = Node(data)  # Create the new node
		cur = self.head
		new_node.next = self.head
		
		if not self.head: #If the linked list is empty
			new_node.next = self.new_node
		else:
			while cur.next != self.head: # While the iterators next is not the head
				cur = cur.next #Continue to the next node
			cur.next = new_node
		self.head = new_node

	def print_list(self):
		cur = self.head

		while cur:
			print(cur.data)
			cur = cur.next
			if cur == self.head:
				break

	def append(self, data):
		# Adding a node to the end of the linked list
		if not self.head:
			# If there is no node in the list, create a new node
			# and set it's next pointer to itself
			self.head = Node(data)
			self.head.next = self.head
		else:
			new_node = Node(data)
			cur = self.head
			while cur.next != self.head:
				cur = cur.next
			cur.next = new_node
			new_node.next = self.head


cllist = CircularLinkedList()
cllist.append('C')
cllist.append('D')
cllist.prepend('B')
cllist.prepend('A')
cllist.print_list()
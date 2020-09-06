class Node():

	def __init__(self, data = None):
		self.data = data
		self.next = None

class LinkedList():

	def __init__(self):
		self.head = None

	def Print(self):
		curr_node = self.head
		while curr_node:
			print(curr_node.data)
			curr_node = curr_node.next

	def insert(self, data):
		
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return	

		tail_node = self.head
		while tail_node.next:
			tail_node =  tail_node.next
		tail_node.next = new_node


ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)

ll.Print()
class Node:
	def __init__(self,dataVal):        # creating a Node
		self.dataVal=dataVal
		self.next=None

class LinkedList:
	def __init__(self):               # Initially initializing the head value to the Null
		self.headVal=None
	
	def append(self,data):         #Adding elements to the end of the linked list   
		new_node=Node(data)
		if self.headVal is None:
			self.headVal=new_node
		else:
			curr_node=self.headVal
			while curr_node.next is not None:
				curr_node=curr_node.next
			curr_node.next=new_node
	def display(self):
		curr_node=self.headVal                   # Displaying the linked list
		if self.headVal is None:
			print("List is Empty")
		while curr_node is not None:
			print(curr_node.dataVal,end="->")
			curr_node=curr_node.next

	def addItemAfter(self,aft,data):            # adding element after the specific node
		curr_node=self.headVal
		new_node=Node(data)
		if self.headVal is None:
			print("Linked list Empty")
		else:
			while curr_node is not None:
				if curr_node.dataVal == aft:
					break;
				curr_node=curr_node.next
			if curr_node is None:
				print("Element is not present")
			else:
				new_node.next = curr_node.next
				curr_node.next=new_node


	def deleteItem(self):
		print("Deleting linked List")           #Deleting each node one by one
		curr_node=self.headVal
		while curr_node is not None:
			print("the data",curr_node.dataVal,"is deleted")
			curr_node.dataVal=None
			curr_node=curr_node.next

	def addItemBefore(self,bef,data):          # adding element before the specific node
		curr_node=self.headVal
		new_node=Node(data)
		while curr_node is not None:
			if curr_node.next.dataVal is bef:
				break
			curr_node=curr_node.next

			if curr_node is None:
				print("Element is not found")
			else:
				new_node.next=curr_node.next
				curr_node.next=new_node

	def reverse(self):
		curr=self.headVal
		prev=None
		while curr:
			next=curr.next
			curr.next=prev
			prev=curr
			curr=next
		self.headVal=prev

	def prepand(self,data):
		new_node=Node(data)
		curr_node=self.headVal
		new_node.next=curr_node
		self.headVal=new_node

		





n=int(input("Enter the node :"))
ll=LinkedList()
for i in range(n):
	ll.append(int(input("Enter the value: ")))
ll.display()
print()
#x1,val1=map(int,input("Enter the after and value :").split())   # This line is for accepting the value from the user
#ll.addItemAfter(x1,val1)
#x2,val2=map(int,input("Enter the before and x values :").split())    # This line is for accepting the value from the user
#ll.addItemBefore(x2,val2)
ll.addItemAfter(3,9)
ll.addItemBefore(2,10)
ll.display()
for i in range(n):
	ll.prepand(int(input("Enter the values: ")))
print()
ll.display()
ll.reverse()
ll.deleteItem()
ll.display()

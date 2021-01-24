# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
		
class LinkedList:

	def __init__(self, head:ListNode):
		self.head = head
		
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		if l1 == None and l2 == None:
			return None
		elif l1 == None and l2 != None:
			return l2
		elif l1 != None and l2 == None:
			return l1
		else:
			if l1.val <= l2.val:
				head = l1
				l1 = l1.next
			else:
				head = l2
				l2 = l2.next
				
			end = head
			while l1 != None and l2 != None:
				if l1.val <= l2.val:
					end.next = l1
					l1 = l1.next
					end = end.next
				else:
					end.next = l2
					l2 = l2.next
					end = end.next
					
			if l1 != None:
				end.next = l1
			else:
				end.next = l2
			return head
				
	def printList(self):
		node = self.head
		while node != None:
			print(node.val, end = " ")
			node = node.next
		print()
			
if __name__ == "__main__":
	
	node3 = ListNode(2)
	node2 = ListNode(1, node3)
	node1 = ListNode(1, node2)
	
	ll1 = LinkedList(node1)
	ll1.printList()
	
	node6 = ListNode(6)
	node5 = ListNode(2, node6)
	node4 = ListNode(0, node5)
	
	ll2 = LinkedList(node4)
	ll2.printList()
	
	ll2.mergeTwoLists(node4, node1)
	ll2.printList()
	
	
	
	
	
	
	
	
	
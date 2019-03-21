class ListNode:
	def __init__(self, x = -1):
		self.value = x
		self.next = None
		self.prev = None

class MyList:
	def __init__(self):
		self.pHead = ListNode()
		self.pTail = ListNode()
		# 下面两行将头和尾关联
		self.pHead.next = self.pTail 
		self.pTail.prev = self.pHead

	def push_back(self, value):
		# 尾节点 保存在最后一个节点的后面
		node = ListNode(value)
		# 新增节点的前面连接尾节点的前面
		node.prev = self.pTail.prev
		self.pTail.prev.next = node
		# 新增节点的后面连接尾节点
		node.next = self.pTail
	 	# 将尾节点连接到node的后面
		self.pTail.prev = node

	def push_front(self, value):
		# 头节点 保存在第一个节点的前面
		node = ListNode(value)
		# 新增节点的后面连接头节点的后面
		node.next = self.pHead.next
		self.pHead.next.prev = node
		# 新增节点的前面连接头节点
		node.prev = self.pHead
		# 将头节点连接到node的前面
		self.pHead.next = node

	def printFromHead(self):
		loop = self.pHead.next
		while loop and loop != self.pTail:
			print(loop.value)
			loop = loop.next

	def printFromTail(self):
		loop = self.pTail.prev
		while loop and loop != self.pHead:
			print(loop.value)
			loop = loop.prev

	def remove_all(self, value):
		loop = self.pHead
		while loop and loop.next and loop.next != self.pTail:
			if loop.next.value == value:
				loop.next = loop.next.next
			loop = loop.next
			

	def countMyList(self):
		number = 0
		loop = self.pHead.next
		while loop and loop != self.pTail:
			number += 1
			loop = loop.next

		return number


mylist = MyList()
mylist.push_back(2)
mylist.push_back(4)
mylist.push_back(6)
mylist.push_front(0)
mylist.push_front(-2)
mylist.push_front(-4)
mylist.push_back(2)

mylist.printFromTail()


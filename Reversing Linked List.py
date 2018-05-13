#Reversing Linked List
#https://pintia.cn/problem-sets/951072707007700992/problems/972813177016877056
#最大N超时
#优化了构建链表还是超时，感觉是输出超时

#节点
class Node:

	def __init__(self,data):
		self.data = data
		self.next = None
#链表
class ListNode:
	def __init__(self):
		self.head = None
	#从后向前添加	
	def appended(self,data):
		temp = Node(data)
		if self.head == None:
			self.head = temp
		else:
			current = self.head
			while current.next != None:
				current = current.next
			current.next = temp
	#从前向后添加		
	def add(self,data):
		temp = Node(data)
		if self.head != None:	
			temp.next = self.head
			self.head = temp
		else:
			self.head = temp
	# #打印链表内容
	# def printList(self):
		# current = self.head
		# while current != None:
			# print(current.data,end=' ')
			# current = current.getNext()
		# print('\n')
	#获取链表长度	
	def getLen(self):
		count = 0
		current = self.head
		while current != None:
			count += 1 
			current = current.next
		return count
#反转列表
def reverseList(oldhead,N,K):
	round = N // K  #反转round轮
	newListNode = ListNode()  #反转结果
	current = oldhead
	for j in range(round):
		i = 0
		tempListNode = ListNode()
		#从前向后添加达到反转目的
		while i<K and current != None:
			tempListNode.add(current.data)
			current = current.next
			i += 1	
		#将反转结果与新链表合并
		if newListNode.head != None:
			temp = newListNode.head
			while temp.next != None:
				temp = temp.next
			temp.next = tempListNode.head
		else:
			newListNode.head = tempListNode.head
	#将新列表后连上剩余未反转内容		
	temp = newListNode.head	
	while temp.next != None:
		temp = temp.next
	temp.next = current
	return newListNode

#按照要求输出结果
def printAnswer(head,doubleList):
	current = head
	for i in range(len(doubleList)):
		if current.data == doubleList[i][1]:
			print(doubleList[i][0],doubleList[i][1],end=' ')
	current = current.next
	while current != None:
		for i in range(len(doubleList)):
			if current.data == doubleList[i][1]:
				print(doubleList[i][0])
				print(doubleList[i][0],doubleList[i][1],end=' ')
		current = current.next
	print('-1')
	
	
def main():
	# init = input().split()
	# address = init[0]
	# N = eval(init[1])
	# K = eval(init[2])
	# doubleList = []
	# preListNode = ListNode()
	# #获取输入内容
	# for i in range(N):
		# temp = input().split()
		# doubleList.append(temp)
	# #将内容写入链表中
	# while address != '-1':
		# for i in range(len(doubleList)):
			# if doubleList[i][0] == address:
				# address = doubleList[i][2]
				# preListNode.appended(doubleList[i][1])
	# N = preListNode.getLen()
	# newListNode = reverseList(preListNode.head,N,K)
	# printAnswer(newListNode.head,doubleList)
	
	init = input().split()
	address = init[0]
	N = eval(init[1])
	K = eval(init[2])
	doubleList = []	
	preListNode = ListNode()
	bigList = [-1] *100001
	for i in range(N):
		temp = input().split()
		doubleList.append(temp)
		bigList[int(temp[0])] = [temp[1],temp[2]]
	while address != '-1':
		preListNode.appended(bigList[int(address)][0])
		address = bigList[int(address)][1]
	N = preListNode.getLen()
	newListNode = reverseList(preListNode.head,N,K)
	printAnswer(newListNode.head,doubleList)
	
main()
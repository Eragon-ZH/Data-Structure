'''
https://pintia.cn/problem-sets/951072707007700992/problems/995137016713310208
最大N超时
'''

class Node():
	def __init__(self,phonenumber):
		self.key = phonenumber
		self.next = None
		self.count = 1

class HashTable():
	def __init__(self,maxsize):
		self.nodeList = [None] * maxsize
	# 求余hash
	def _hash(self,key):
		return key%len(self.nodeList)
	
	def insertNode(self,phonenumber):
		# 用电话号码最后5位作为识别码
		key = phonenumber % 100000
		hash = self._hash(key)
		if self.nodeList[hash] == None:
			newnode = Node(phonenumber)
			self.nodeList[hash] = newnode
		else:
			tep = self.nodeList[hash]
			while True:
				if phonenumber == tep.key:
					tep.count += 1
					return
				if tep.next == None:
					break
				tep = tep.next
			newnode = Node(phonenumber)
			tep.next = newnode

def findMostPhoneNumber(hashtable):
	count = 0
	people = 0
	phonenumber = None
	# 遍历整个散列表
	for i in hashtable.nodeList:
		if i != None:
			tep = i
			while True:
				# 得到count最大phonenumber
				if tep.count > count:
					count = tep.count
					people = 1
					phonenumber = tep.key
				# count相同的记录最小的phonenumber，并记录相同count的人数
				elif tep.count == count:
					people += 1
					if tep.key < phonenumber:
						phonenumber = tep.key
				if tep.next == None:
					break
				tep = tep.next
	return count,people,phonenumber
			
def nextPrime(n):
	while True:
		if isPrime(n):
			return n
		n += 1
	
def isPrime(x):
	if x == 1 or x == 2 or x == 3:
		return True
	isPrime = True
	for i in range(3,x):
		if x % i == 0:
			isPrime = False
			break
	return isPrime
	
def main():
	N = int(input())
	# 散列表大小为2倍的N的下一个质数
	hashtable = HashTable(nextPrime(2*N))
	for i in range(N):
		tep = input().split()
		a = int(tep[0])
		b = int(tep[1])
		hashtable.insertNode(a)
		hashtable.insertNode(b)
	# for i in range(len(hashtable.nodeList)):
		# if hashtable.nodeList[i] != None:
			# print(i)
			# tep = hashtable.nodeList[i] 
			# while True:
				# print(tep.key,tep.count,tep.next)
				# if tep.next == None:
					# break
				# tep = tep.next
	count,people,phonenumber = findMostPhoneNumber(hashtable)
	if people > 1:
		print(phonenumber,count,people)
	else:
		print(phonenumber,count)
		
if __name__ == '__main__':
	main()
	
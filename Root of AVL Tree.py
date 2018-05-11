#https://pintia.cn/problem-sets/951072707007700992/problems/977489194356715520
#实现了AVLTree的put功能
#没有实现delete功能

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		self.height = 0
		
class AVLTree:
	def __init__(self):
		self.root = None
		
	def height(self,node):
		if node is None:
			return -1
		else:
			return node.height
	#破坏者在被破坏者的左子树的左子树上	
	def LLrotate(self,node):
		temp = node.left
		node.left = temp.right
		temp.right = node
		node.height = max(self.height(node.left),self.height(node.right))+1
		temp.height = max(self.height(temp.left),self.height(node.right))+1
		return temp
	
	def RRrotate(self,node):
		temp = node.right
		node.right = temp.left
		temp.left = node
		node.height = max(self.height(node.left),self.height(node.right))+1
		temp.height = max(self.height(node.left),self.height(node.right))+1
		return temp
	#破坏者在被破坏者的右子树的左子树上
	#先做一次LL旋转再做一次RR旋转
	def RLrotate(self,node):
		node.right = self.LLrotate(node.right)
		return self.RRrotate(node)
		
	def LRrotare(self,node):
		node.left = self.RRrotate(node.left)
		return self.LLrotate(node)
		
	def put(self,data):
		if not self.root:
			self.root = Node(data)
		else:
			self.root = self._put(data,self.root)
	def _put(self,data,node):
		if node is None:
			node = Node(data)
		elif data < node.data:
			node.left = self._put(data,node.left)
			if (self.height(node.left) - self.height(node.right)) == 2:
				if data < node.left.data:
					node = self.LLrotate(node)
				else:
					node = self.LRrotare(node)
		elif data > node.data:
			node.right = self._put(data,node.right)
			if (self.height(node.right) - self.height(node.left)) == 2:
				if data < node.right.data:
					node = self.RLrotate(node)
				else:
					node = self.RRrotate(node)
			
		node.height = max(self.height(node.left),self.height(node.right)) + 1
		return node
			
def main():
	N = input()
	li = input().split()
	tree = AVLTree()
	for i in li:
		tree.put(int(i))
	print(tree.root.data)
main()
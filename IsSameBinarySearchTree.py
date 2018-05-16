#是否是同一棵二叉搜索树
#https://pintia.cn/problem-sets/951072707007700992/problems/977489131995787264
# 最大N，多组合没过

#树
class Tree:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		self.tag = 0
#递归插入
def insert(root,data):
	if root is None:
		root = Tree(data)
	else:
		if data < root.data:
			root.left = insert(root.left,data)
		elif data > root.data:
			root.right = insert(root.right,data)
	return root
#将Tag重置
def setTag(tree):
	if tree != None:
		tree.tag = 0
		setTag(tree.left)
		setTag(tree.right)
#根据序列生成树		
def makeTree():
	li = input().split()
	tree = Tree(li[0])
	for i in range(1,len(li)):
		tree = insert(tree,li[i])
	return tree		
#从root查找一个数字，查到后将其的tag设为1
#如果途经了tag为0的数字，说明不是同一棵树
def check(tree,a):
	if tree.tag == 1:
		if a < tree.data:
			return check(tree.left,a)
		elif a > tree.data:
			return check(tree.right,a)
		elif a == tree.data:
			return True
	elif tree.tag == 0:
		if a == tree.data:
			tree.tag = 1
			return True
		else:
			return False
#按顺序对每一个数字check
def isSameTree(tree):
	li = input().split()
	for i in li:
		if check(tree,i) == False:
			return False
	return True
	
def main():
	#接收到0后退出
	while True:
		li = input().split()
		K = eval(li[0])
		if K == 0:
			break
		L = eval(li[1])
		tree = makeTree()
		# printTree(tree)
		for i in range(L):
			setTag(tree)
			if isSameTree(tree):
				print('Yes')
			else:
				print('No')
main()
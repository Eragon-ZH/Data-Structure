'''
Tree Traversals Again
https://pintia.cn/problem-sets/951072707007700992/problems/975887458772324352
压栈顺序即为先序遍历
出栈顺序即为中序遍历
先序第一个为根，找到根在中序里的位置，左边即为左子树，右边即为右子树
其实可以不建树，直接输出后序遍历结果，先序第一个就是后序最后一个，再对左右子树递归调用
N=30复杂组合没过
'''

#定义树类型
class Tree:
	def __init__(self,data,left,right):
		self.data = data
		self.left = left
		self.right = right
#获取输入		
def getList():
	K = eval(input())
	#先序数列
	preList = []
	#中序数列
	inList = []
	seq = []
	for i in range(2*K):
		li = input()
		if li[1] == 'u':
			preList.append(eval(li[-1]))
			seq.append(eval(li[-1]))
		else:
			inList.append(seq.pop())
	return preList,inList
#构建树
def makeTree(preorder,inorder):
	#如果长度为0则没有子树返回
	if len(preorder) == 0:
		return None
	#获取父结点的值
	rootdata = preorder[0]
	index = inorder.index(rootdata)
	#用父结点将中序数列分为左右两部分即为左子树和右子树
	#递归调用
	left = makeTree(preorder[1:index+1],inorder[:index])
	right = makeTree(preorder[index+1:],inorder[index+1:])
	#创建结点
	return Tree(rootdata,left,right)
	
def Postorder(tree,root):
	#后序遍历并格式化输出
	global Result
	if tree != None and tree.data != root:
		Postorder(tree.left,root)
		Postorder(tree.right,root)
		print(tree.data,end = ' ')
	if tree != None and tree.data == root:
		Postorder(tree.left,root)
		Postorder(tree.right,root)
		print(tree.data,end = '')
	
def main():
	preorder,inorder = getList()
	tree = makeTree(preorder,inorder)
	root = tree.data
	Postorder(tree,root)	
	
main()